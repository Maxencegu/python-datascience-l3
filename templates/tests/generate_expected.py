"""
Script ENSEIGNANT — génère le fichier JSON des outputs attendus à partir du notebook de correction.
À exécuter une fois après avoir finalisé et exécuté le notebook de correction.

Usage : python generate_expected.py <tdXX_correction.ipynb> <tdXX_expected.json> [tdXX_enonce.ipynb]
Exemple : python generate_expected.py td03_correction.ipynb td03_expected.json td03_enonce.ipynb

Si l'énoncé est fourni, le script vérifie que chaque index retenu désigne, dans l'énoncé,
une cellule de code qui correspond à celle de la correction (même première ligne).
Les tests étant indexés par position, un décalage entre énoncé et correction ferait
échouer les tests de tous les étudiants.

Le fichier JSON produit est à déposer dans templates/tests/ du dépôt du cours.
"""
import sys
import json
import nbformat

if len(sys.argv) not in (3, 4):
    print("Usage : python generate_expected.py <correction.ipynb> <output.json> [enonce.ipynb]")
    sys.exit(1)

nb_path, out_path = sys.argv[1], sys.argv[2]
enonce_path = sys.argv[3] if len(sys.argv) == 4 else None

with open(nb_path, encoding="utf-8") as f:
    nb = nbformat.read(f, as_version=4)

enonce = None
if enonce_path:
    with open(enonce_path, encoding="utf-8") as f:
        enonce = nbformat.read(f, as_version=4)
    if len(enonce.cells) != len(nb.cells):
        print(f"⚠️  Énoncé : {len(enonce.cells)} cellules, correction : {len(nb.cells)} cellules")

# Sorties sans intérêt pour les tests (affichages HTML, images)
OBJETS_AFFICHAGE = ("<IPython.core.display.", "<IPython.lib.display.")


def premiere_ligne(cell):
    return cell.source.lstrip().split("\n")[0]


expected = {}
skipped = 0
erreurs = []

for i, cell in enumerate(nb.cells):
    if cell.cell_type != "code" or not cell.outputs:
        continue
    parts = []
    for out in cell.outputs:
        if out.output_type == "error":
            erreurs.append(f"  Cellule {i} : {out.ename}: {out.evalue}")
        elif out.output_type == "stream":
            parts.append(out.text)
        elif out.output_type in ("execute_result", "display_data"):
            texte = out.get("data", {}).get("text/plain", "")
            if not texte.startswith(OBJETS_AFFICHAGE):
                parts.append(texte)
    text = "".join(parts).strip()
    if not text:
        skipped += 1
        continue
    if enonce is not None:
        if i >= len(enonce.cells) or enonce.cells[i].cell_type != "code":
            erreurs.append(f"  Cellule {i} : pas une cellule de code dans l'énoncé (décalage énoncé/correction ?)")
            continue
        if premiere_ligne(enonce.cells[i]) != premiere_ligne(cell):
            print(f"⚠️  Cellule {i} : première ligne différente — énoncé {premiere_ligne(enonce.cells[i])!r}"
                  f" / correction {premiere_ligne(cell)!r}")
    expected[str(i)] = text

if erreurs:
    print("❌ JSON non généré :")
    print("\n".join(erreurs))
    sys.exit(1)

with open(out_path, "w", encoding="utf-8") as f:
    json.dump(expected, f, indent=2, ensure_ascii=False)
    f.write("\n")

print(f"✅ {len(expected)} cellules avec output indexées dans {out_path}")
if skipped:
    print(f"   ({skipped} cellules ignorées : sans output ou affichage HTML/image uniquement)")
if enonce is None:
    print("   ⚠️  Énoncé non fourni : alignement des index non vérifié")
print()
print("Pensez à relire le JSON et à supprimer les réponses libres")
print("(texte saisi par l'étudiant, ex. \"OUI\"/\"NON\") : elles ne se comparent pas au caractère près.")

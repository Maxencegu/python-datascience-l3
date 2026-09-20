"""
Runner universel de tests pour les notebooks étudiants.
Téléchargé automatiquement par le workflow GitHub Actions au moment de l'exécution.
Usage : python run_tests.py <tdXX_enonce.ipynb> <tdXX_expected.json>
"""
import os
import sys
import json
import nbformat
from nbconvert.preprocessors import ExecutePreprocessor

if len(sys.argv) != 3:
    print("Usage : python run_tests.py <notebook.ipynb> <expected.json>")
    sys.exit(1)

nb_path, expected_path = sys.argv[1], sys.argv[2]

if not os.path.exists(nb_path):
    notebooks = sorted(
        os.path.relpath(os.path.join(racine, f))
        for racine, dossiers, fichiers in os.walk(".")
        if ".git" not in racine.split(os.sep)
        for f in fichiers if f.endswith(".ipynb")
    )
    print(f"❌ Notebook {nb_path} introuvable à la racine du dépôt.")
    if notebooks:
        print(f"   Notebooks présents : {', '.join(notebooks)}")
        print(f"   Déposez votre notebook à la racine du dépôt, sous le nom exact {nb_path}")
    sys.exit(1)

print(f"📓 Exécution de {nb_path}...")

with open(nb_path, encoding="utf-8") as f:
    nb = nbformat.read(f, as_version=4)

ep = ExecutePreprocessor(timeout=300, kernel_name="python3")
try:
    ep.preprocess(nb, {"metadata": {"path": "."}})
except Exception as e:
    print(f"❌ Le notebook a planté pendant l'exécution :\n   {e}")
    sys.exit(1)

print("✅ Notebook exécuté sans erreur\n")
print("🔍 Vérification des résultats...\n")

with open(expected_path, encoding="utf-8") as f:
    expected = json.load(f)

errors = []
for cell_idx, exp in expected.items():
    idx = int(cell_idx)
    if idx >= len(nb.cells) or nb.cells[idx].cell_type != "code":
        errors.append(
            f"  Cellule {cell_idx}\n"
            f"    la cellule n'existe pas ou n'est pas une cellule de code — "
            f"avez-vous ajouté ou supprimé des cellules dans le notebook ?"
        )
        continue
    cell = nb.cells[idx]
    parts = []
    for out in cell.outputs:
        if out.output_type == "stream":
            parts.append(out.get("text", ""))
        elif out.output_type in ("execute_result", "display_data"):
            texte = out.get("data", {}).get("text/plain", "")
            # Même filtre que generate_expected.py : affichages HTML/image ignorés
            if not texte.startswith(("<IPython.core.display.", "<IPython.lib.display.")):
                parts.append(texte)
    actual = "".join(parts).strip()
    if actual != exp.strip():
        errors.append(
            f"  Cellule {cell_idx}\n"
            f"    attendu  : {exp.strip()!r}\n"
            f"    obtenu   : {actual!r}"
        )

if errors:
    print(f"❌ {len(errors)} test(s) échoué(s) :\n")
    for e in errors:
        print(e)
    sys.exit(1)

print(f"✅ Tous les tests passent ({len(expected)} cellules vérifiées)")

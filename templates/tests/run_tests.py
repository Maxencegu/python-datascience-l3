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


def _titre_cellule(cell, idx):
    """Retourne le titre lisible de la cellule (# @title ou première ligne utile)."""
    source = cell.source if isinstance(cell.source, str) else "".join(cell.source)
    for ligne in source.splitlines():
        ligne = ligne.strip()
        if ligne.startswith("# @title"):
            titre = ligne.replace("# @title", "").strip()
            if titre:
                return titre
        if ligne.startswith("#") and len(ligne) > 2:
            return ligne.lstrip("# ").strip()
    for ligne in source.splitlines():
        if ligne.strip() and not ligne.strip().startswith("#"):
            return ligne.strip()[:70]
    return f"cellule {idx}"


def _extrait_code(cell, max_lignes=3):
    """Premières lignes de code significatives (sans commentaires ni lignes vides)."""
    source = cell.source if isinstance(cell.source, str) else "".join(cell.source)
    lignes = [
        l.rstrip() for l in source.splitlines()
        if l.strip() and not l.strip().startswith("#")
    ]
    extrait = "\n       ".join(lignes[:max_lignes])
    if len(lignes) > max_lignes:
        extrait += f"\n       … ({len(lignes) - max_lignes} ligne(s) supplémentaire(s))"
    return extrait


errors = []
for cell_idx, exp in expected.items():
    idx = int(cell_idx)
    if idx >= len(nb.cells) or nb.cells[idx].cell_type != "code":
        errors.append(
            f"  ❌ Cellule {cell_idx} introuvable ou déplacée\n"
            f"     → Avez-vous ajouté ou supprimé des cellules dans le notebook ?"
        )
        continue
    cell = nb.cells[idx]
    parts = []
    for out in cell.outputs:
        if out.output_type == "stream":
            parts.append(out.get("text", ""))
        elif out.output_type in ("execute_result", "display_data"):
            texte = out.get("data", {}).get("text/plain", "")
            if not texte.startswith(("<IPython.core.display.", "<IPython.lib.display.")):
                parts.append(texte)
    actual = "".join(parts).strip()
    if actual != exp.strip():
        titre = _titre_cellule(cell, idx)
        code = _extrait_code(cell)
        raison = "cellule jamais exécutée" if not actual else None
        ligne_attendu = f"     Attendu  : {exp.strip()!r}"
        ligne_obtenu = f"     Obtenu   : {actual!r}" + (f"  ← {raison}" if raison else "")
        bloc = f"  ❌ {titre}\n"
        if code:
            bloc += f"     Code     : {code}\n"
        bloc += f"{ligne_attendu}\n{ligne_obtenu}"
        errors.append(bloc)

if errors:
    print(f"❌ {len(errors)} test(s) échoué(s) :\n")
    for e in errors:
        print(e)
        print()
    sys.exit(1)

print(f"✅ Tous les tests passent ({len(expected)} cellules vérifiées)")

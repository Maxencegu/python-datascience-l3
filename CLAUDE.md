# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Ce que contient ce dépôt

Dépôt enseignant public du cours **Python & Data Science** (L3 / M1 Économie, UPJV Amiens). Il contient les notebooks de TD, les jeux de données, la documentation et les ressources pédagogiques. Ce n'est pas un projet logiciel : il n'y a pas de commandes de build, de lint ou de tests à exécuter localement. Les tests automatiques sont exécutés dans les dépôts étudiants via GitHub Actions.

La référence complète des décisions pédagogiques et techniques est dans **PLAN.md**.

## Structure

```
assignments/tdXX_nom_du_td/     ← notebooks d'énoncé, organisés par TD
    images/                     ← infographies PNG co-localisées avec le TD
datasets/                       ← jeux de données légers partagés entre TD
docs/                           ← guides techniques (Colab, Git, GitHub, erreurs)
faq/                            ← questions fréquentes étudiants
projects/                       ← consignes mini-projets (MP1, MP2) et projets groupe
resources/                      ← fiches mémo et ressources complémentaires
templates/                      ← modèles de fichiers (solutions.py, tests.yml, etc.)
assets/                         ← visuels du dépôt (banner, images README)
```

Les corrigés ne sont **jamais** dans ce dépôt public. Ils sont conservés dans un dépôt privé séparé ou sur Google Drive, et publiés dans `assignments/tdXX/` après l'échéance.

## Convention de nommage

| Élément | Convention | Exemple |
|---------|-----------|---------|
| Dossier TD | `tdXX_nom_descriptif` | `td01_introduction_a_git` |
| Notebook énoncé | `tdXX_enonce.ipynb` | `td01_enonce.ipynb` |
| Notebook correction | `tdXX_correction.ipynb` | `td01_correction.ipynb` |
| Infographies | `NN_nom_descriptif.png` | `01_gestion_de_versions.png` |
| Données | snake_case, année si pertinent | `salaires_2023.csv` |

## Structure d'un notebook Colab

Chaque notebook commence par :
1. Un badge **Open in Colab** en première cellule
2. Une cellule `# @title ⚙️ Configuration` (cachée) qui définit la fonction helper d'infographie et recrée l'environnement si nécessaire
3. Les sections pédagogiques

Badge Open in Colab :
```markdown
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Maxencegu/python-datascience-l3/blob/main/assignments/tdXX_nom/tdXX_enonce.ipynb)
```

Fonction helper infographie (à adapter par TD) :
```python
# @title ⚙️ Configuration des ressources (ne pas modifier)
from IPython.display import Image, display

BASE_URL = "https://raw.githubusercontent.com/Maxencegu/python-datascience-l3/main/assignments/tdXX_nom/images/"

def afficher_infographie(nom_fichier, largeur=1300):
    display(Image(url=BASE_URL + nom_fichier, width=largeur))
```

## Introduction d'un notebook TD

La cellule Markdown d'introduction suit toujours ce plan :
1. Badge Open in Colab
2. `# **Introduction**`
3. Rappel du TD précédent (ce que l'étudiant sait déjà)
4. Le problème que ce TD va résoudre (accroche)
5. Présentation des concepts clés (en **gras**)
6. Liste `Dans ce TD, vous apprendrez à :`
7. Phrase de clôture `À l'issue de cette séance, vous serez capables de…`

Exemple (TD05) :
```markdown
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Maxencegu/python-datascience-l3/blob/main/assignments/td05_matplotlib_dictionnaires_et_pandas/td05_enonce.ipynb)

# **Introduction**

Au TD précédent, vous avez découvert les **fonctions** et **NumPy**.
Vous savez maintenant encapsuler une opération dans une fonction réutilisable,
importer un module, et effectuer des calculs vectorisés sur des tableaux NumPy.

Mais un tableau NumPy impose un type unique pour toutes ses valeurs.
Comment stocker à la fois le nom d'un pays, sa capitale et sa population ?
Et une fois les données en main, comment les visualiser rapidement pour en extraire du sens ?

C'est exactement ce que vous allez apprendre dans ce TD, avec trois outils complémentaires.

**Matplotlib** est la bibliothèque de référence pour la visualisation en Python.
Avec quelques lignes de code, vous pouvez tracer des courbes, des nuages de points
et des histogrammes — et les personnaliser entièrement.

Les **dictionnaires** permettent d'associer des clés à des valeurs de types variés.
Ils sont indispensables pour représenter des données structurées comme un profil pays,
et constituent la brique de base pour construire un DataFrame Pandas.

**Pandas** apporte la structure de données tabulaire que NumPy ne peut pas offrir :
le **DataFrame**, un tableau à deux dimensions où chaque colonne peut avoir son propre type.
C'est l'outil central de tout data scientist Python.

Dans ce TD, vous apprendrez à :
- tracer des graphiques (courbes, nuages de points, histogrammes) avec Matplotlib ;
- personnaliser vos visualisations (titres, axes, couleurs, tailles) ;
- créer et manipuler des dictionnaires (accès, ajout, suppression, imbrication) ;
- construire un DataFrame Pandas depuis un dictionnaire ou un fichier CSV ;
- sélectionner des données dans un DataFrame avec `[ ]`, `loc` et `iloc`.

À l'issue de cette séance, vous serez capables de charger un jeu de données réel,
d'en extraire les observations et variables qui vous intéressent,
et de produire une visualisation exploitable en quelques lignes de code.
```

## Création des infographies

Les infographies sont générées via un script Python/Playwright : HTML écrit directement dans le script → `page.set_content()` → screenshot PNG. **Pas de fichier HTML intermédiaire.**

Script type (à adapter) :
```python
from playwright.sync_api import sync_playwright

html_content = """<!DOCTYPE html><html lang="fr"><head>...</head><body>...</body></html>"""

OUTPUT = r"assignments/tdXX_nom/images/NN_nom_pro.png"

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page(viewport={"width": 1200, "height": 900}, device_scale_factor=2)
    page.set_content(html_content, wait_until="networkidle")
    page.screenshot(path=OUTPUT, full_page=True)
    browser.close()
```

**Système de design (thème sombre, à reproduire fidèlement) :**
- Fond : `#0d1117` — Cartes : `#161b22` — Bordures : `#21262d`
- Texte principal : `#e6edf3` — Texte secondaire : `#8b949e`
- Breadcrumb (en-tête) : `#58a6ff`, uppercase, letter-spacing 0.15em
- Accentuation des cartes (barre top de 3px) : bleu `#1f6feb`, violet `#8b5cf6`, vert `#3fb950`, orange `#d29922`, rouge `#f85149`
- Code inline : `color: #79c0ff`, `background: #0d1117`, bordure `#30363d`
- Alerte rouge : `background: #200d0d`, bordure `#f85149`
- Viewport 1200×900 + `device_scale_factor=2` → PNG 2400px de large
- Breadcrumb : `TD2 · GITHUB · PYTHON DATA SCIENCE — UPJV AMIENS`

Nommage des fichiers PNG : `NN_nom_descriptif_pro.png` (suffixe `_pro` pour la version finale).

## Pattern d'exercice interactif (3 cellules)

Tout exercice suit ce schéma fixe :

**Cellule 1 — Setup** (`# @title ⚙️ Préparation de l'exercice (exécuter d'abord)`) : crée l'environnement (dossiers, fichiers, état initial Git). Toujours commencer par `os.chdir("/content")`. Supprimer les variables de l'exercice précédent avec `try: del var / except NameError: pass`.

**Cellule 2 — Exercice** (`# @title 🔧 Exercice — Titre`) : instructions en commentaires avec le format ci-dessous, placeholders `____` (4 underscores) à remplacer par l'étudiant. Ne jamais utiliser `___` (3 underscores) : dans IPython/Colab c'est une variable d'historique (vaut `''`), un trou non rempli ne lèverait pas de `NameError`.

**Cellule 3 — Validation** (`# @title ✅ Vérification`) : vérifie l'état du système et affiche un retour avec ✅ / ❌. Ne jamais afficher `💡 Indice` quand tout est ✅.

Format des commentaires dans la cellule exercice :
```python
# @title 🔧 Exercice — Titre
# ================================================================
#  EXERCICE — Description courte                      [ N étapes ]
# ================================================================
#
# Contexte / rappel de situation
#
# ----------------------------------------------------------------
# Étape 1/N — Consigne
# ----------------------------------------------------------------
variable = ____

# ----------------------------------------------------------------
# Étape 2/N — Consigne
# ----------------------------------------------------------------
____
```

**Règles critiques pour les exercices shell :**
- `%cd dossier` (pas `!cd`) pour les changements de répertoire persistants
- Commentaires **au-dessus** des commandes magiques `%`, jamais en fin de ligne
- `result = !commande` pour capturer la sortie dans une variable testable
- `!ls -1` plutôt que `!ls` pour un fichier par ligne (validation plus fiable)
- La validation utilise `os.listdir()` et `os.getcwd()` plutôt que de parser la sortie de `ls`

**Règles d'isolation entre exercices :**
- Chaque setup commence par `os.chdir("/content")`
- Si l'exercice utilise un dossier Git : `shutil.rmtree(repo)` avant `os.makedirs(repo)`
- Supprimer les variables réutilisées : `try: del journal / except NameError: pass` à la fin du setup
- `git config color.ui false` dans le setup + fonction `strip_ansi()` dans la validation pour éviter les faux négatifs sur les codes ANSI

**Pattern QCM (exercice à choix multiples) :**

Setup minimal :
```python
# @title ⚙️ Préparation de l'exercice (exécuter d'abord)
try:
    del reponse
except NameError:
    pass
print("✅ Environnement prêt")
```

Exercice :
```python
# @title 🔧 Exercice — Titre du QCM
# ================================================================
#  EXERCICE — Titre                                   [ 1 étape ]
# ================================================================
#
# Question posée ?
#
#   1 — Option A
#   2 — Option B
#   3 — Option C  (correcte)
#   4 — Option D
#
# ----------------------------------------------------------------
# Entrez le numéro de la bonne réponse (1, 2, 3 ou 4)
# ----------------------------------------------------------------
reponse = ____
```

Validation :
```python
# @title ✅ Vérification
print("Résultats :\n")

EXPLICATIONS = {
    1: "Explication pourquoi 1 est faux.",
    2: "Explication pourquoi 2 est faux.",
    3: "Correct ! Explication.",
    4: "Explication pourquoi 4 est faux.",
}

try:
    r = int(reponse)
    if isinstance(reponse, bool) or r != float(reponse):
        raise ValueError  # refuse True/False et les nombres non entiers (3.7)
    if r == 3:
        print(f"  ✅ Bonne réponse ({r}) : {EXPLICATIONS[r]}")
    elif r in EXPLICATIONS:
        print(f"  ❌ Réponse {r} incorrecte : {EXPLICATIONS[r]}")
    else:
        print(f"  ❌ Réponse non reconnue : {reponse!r} — attendu un nombre entre 1 et 4")
except NameError:
    print("  ❌ reponse n'est pas défini — attribuez un nombre à la variable reponse")
except (ValueError, TypeError):
    print(f"  ❌ reponse doit être un nombre (1, 2, 3 ou 4) — valeur reçue : {reponse!r}")
```

## Règles de contenu (dépôt public)

Ne jamais ajouter dans ce dépôt :
- Liste nominative des étudiants, notes, adresses e-mail, numéros étudiants
- Corrigés avant l'échéance
- Clés API ou tokens
- Données personnelles ou confidentielles

## Programme (année commune L3/M1 2026-2027)

**8 TD de contenu + 1 examen final = 9 séances × 2h = 18h.**
Le TD07 intègre : (1) l'étude de cas "statistiques pirates" (nombres aléatoires, marche aléatoire, simulation, Matplotlib) puis (2) le mini-projet 1 en binôme démarré en séance et **terminé à la maison**. **Pas de quiz de fin de séance pour le TD07** (séance trop chargée).

**Barème TD07 :** 10 pts présence + 20 pts étude de cas (en séance) + 30 pts mini-projet 1 (rendu à la maison) = **60 pts**.

| Séance | Contenu | Dossier |
|--------|---------|---------|
| TD1 | Introduction à Git | `td01_introduction_a_git` |
| TD2 | Introduction à GitHub | `td02_introduction_aux_concepts_de_github` |
| TD3 | Les bases de Python | `td03_bases_de_python` |
| TD4 | Les fonctions, modules et NumPy | `td04_fonctions_et_numpy` |
| TD5 | Matplotlib, dictionnaires et Pandas | `td05_matplotlib_dictionnaires_et_pandas` |
| TD6 | Logique, flux de contrôle, filtrage et boucles | `td06_Logique_flux_de_controle_filtrage_et_boucles` |
| TD7_MP1 | Étude de cas "statistiques pirates" + Mini-projet 1 en binôme | `td07_mp1_etude_de_cas_et_mini_projet` |
| TD8 | Pandas : agrégation et transformation | `td08_pandas_agregation_et_transformation` |
| Examen | Examen final individuel | `assignments/examen_final/` (gitignorée jusqu'au jour J) |

**Workflow d'une séance (à ne pas modifier sans accord) :**
GitHub → Correction TD précédent (à partir TD2) → Google Forms présence (10 pts) → Colab → Exercices (20 pts) → Sauvegarde GitHub sur branche `dev_tdXX` (à partir TD2) → GitHub Actions sur branche (à partir TD3) → Pull Request + review collègue → Merge main (à partir TD3) → Quiz fin de séance (10 pts, à partir TD3) incluant le renseignement de l'URL du dépôt étudiant (pour automatiser la correction)

**Gestion du temps en séance :**
Le quiz de fin de séance est obligatoire et se ferme à la fin du TD. Les étudiants doivent sauter des exercices si nécessaire pour avoir le temps de faire le quiz. Tout le notebook doit être terminé avant le prochain TD.

**Remarques importantes :**
- Les notebooks TD sont modifiés progressivement : ne jamais remplacer un notebook TD existant intégralement sans confirmation explicite
- Le notebook de correction (`tdXX_correction.ipynb`) est dans `.gitignore` — à stocker sur Google Drive jusqu'à la date de publication

## Workflow étudiant (à partir du TD03)

Les étudiants disposent d'un dépôt personnel `upjv-python-datascience` créé pendant le TD02.

**Convention de branche :** `dev_tdXX` (ex. : `dev_td03`, `dev_td04`)

**Cycle par TD :**
1. Créer la branche `dev_tdXX` depuis `main`
2. Travailler sur le notebook dans Colab
3. Uploader le notebook sur la branche `dev_tdXX`
4. GitHub Actions (écrits par l'enseignant) vérifient automatiquement le notebook sur la branche
5. Quand les tests passent → ouvrir une Pull Request vers `main`
6. Un collègue valide la PR (reviewer obligatoire — règle de protection configurée en TD02)
7. Merge sur `main`

**Configuration mise en place en TD02 :**
- Protection de la branche `main` : 1 reviewer obligatoire avant merge

**`requirements.txt` inutile** : les étudiants travaillent sur Colab, qui dispose de numpy, pandas, matplotlib et seaborn préinstallés. Ne pas inclure dans les exercices.

## GitHub Actions — tests automatiques (à partir du TD03)

### Architecture

```
templates/tests/
  tests_td.yml          ← workflow générique copié UNE FOIS par l'étudiant dans son repo
  run_tests.py          ← runner universel téléchargé par Actions au moment de l'exécution
  generate_expected.py  ← script ENSEIGNANT pour générer le JSON depuis la correction
  td03_expected.json    ← outputs attendus TD03 ✅
  td04_expected.json    ← outputs attendus TD04 ✅
  td05_expected.json    ← outputs attendus TD05 ✅
  td06_expected.json    ← outputs attendus TD06 ✅
  td07_expected.json    ← outputs attendus TD07 partie 1 uniquement (MP exclu) ✅
  td08_expected.json    ← outputs attendus TD08 ✅
templates/dashboard_etudiants.py  ← script enseignant : tableau de bord HTML de la promo
```

## Tableau de bord enseignant

`templates/dashboard_etudiants.py` agrège tout le suivi de la promo et écrit un
tableau de bord HTML autonome.

```
python templates/dashboard_etudiants.py            # tous les TD
python templates/dashboard_etudiants.py --td td03  # un seul TD
python templates/dashboard_etudiants.py --refresh  # ignore le cache GitHub (TTL 15 min)
python templates/dashboard_etudiants.py --offline  # aucune requête réseau
```

Prérequis : `gh auth login`. `openpyxl` seulement si les exports sont en `.xlsx`.

**Entrées — toutes dans `réponses/` (dossier gitignoré, données nominatives) :**

| Fichier | Rôle |
|---------|------|
| `TDxx - Feuille de Présence.csv` (ou `.zip`, `.xlsx`) | export Google Forms, présence |
| `TDxx - Quiz.csv` (ou `.zip`, `.xlsx`) | export Google Forms, score du quiz + URL du dépôt |
| `etudiants.csv` | annuaire `email,nom,numero,username`, complété automatiquement depuis l'URL du quiz, éditable à la main |

Le TD est déduit du nom de fichier (`TD03`, `td3`…), les colonnes sont reconnues
par mots-clés dans l'en-tête — aucun format strict à respecter.

**Ce qui est vérifié pour chaque étudiant et chaque TD :**
- présence et score du quiz (exports Google Forms)
- `tdXX_enonce.ipynb` présent sur `main`
- sorties des cellules comparées à `templates/tests/tdXX_expected.json` ; pour le
  TD01 et le TD02 (pas de JSON d'attendus), lecture des cellules `✅ Vérification`
  et détection des `❌` et des placeholders `____` restants
- cycle Git : branche `dev_tdXX`, Pull Request, approbation **par un tiers**
  (l'auto-approbation est signalée), merge, suppression de la branche,
  conclusion des GitHub Actions, dates de création et de merge

**Notes** — barème du README : 10 pts présence + 20 pts notebook + 10 pts quiz
(TD07 : 10 + 20 + 30 pts de mini-projet, pas de quiz). Les 20 pts du notebook sont
proportionnels aux cellules correctes.

**Sortie** : `réponses/dashboard.html`, autonome, avec recherche, filtre par TD,
filtres « problèmes uniquement » et « sans dépôt », tri par colonne et détail
par TD au clic. **Contient des données nominatives : ne jamais le committer.**

La vérification du cycle Pull Request du TD02 ne peut pas être verte dans le
notebook déposé (elle s'exécute après l'upload) : elle est exclue de l'audit des
cellules et contrôlée via l'API GitHub.

### Principe de test

- Les tests vérifient les **outputs des cellules** (pas les variables) → pas de collision entre cellules
- Le fichier `tdXX_expected.json` mappe `"index_cellule" → "output_attendu"` (string stripé)
- Le runner est téléchargé depuis le dépôt du cours au runtime → valeurs cachées des étudiants
- Le workflow se déclenche sur tout push vers une branche `dev_*` (aussi `Dev_*`, `DEV_*`) et sur toute PR vers `main`
- Le nom du TD est déduit automatiquement du nom de branche : `dev_td03` → `td03` (insensible à la casse ; une branche `dev_*` mal nommée, ex. `dev_td3`, fait échouer le job)
- Tests ignorés (job vert) : branche qui ne commence pas par `dev_` (ex. PR `examen_final`), TD sans `tdXX_expected.json` (TD01, TD02, TD non publié), ou push sans aucun notebook du TD, à quelque profondeur que ce soit (branche tout juste créée). Un notebook du TD mal nommé ou mal placé (`Copie de td03_enonce.ipynb`, `TD3.ipynb`, `TD03/td03_enonce.ipynb`) fait échouer le job avec le nom attendu, sur push comme sur PR

### Workflow côté enseignant (par TD)

1. Finaliser et exécuter le notebook de correction (`tdXX_correction.ipynb`)
2. Générer le JSON : `python templates/tests/generate_expected.py tdXX_correction.ipynb tdXX_expected.json tdXX_enonce.ipynb` (le 3e argument vérifie que chaque index désigne la même cellule de code dans l'énoncé — un décalage ferait échouer tous les étudiants)
3. Relire le JSON : supprimer les cellules de préparation et les réponses libres (texte saisi par l'étudiant, ex. `"OUI"`) ; les affichages HTML/image sont déjà filtrés
4. Déposer `tdXX_expected.json` dans `templates/tests/` du dépôt du cours
5. Pusher → les tests s'activent automatiquement pour tous les étudiants déjà configurés

### Workflow côté étudiant (une seule fois, en TD02)

1. Récupérer `templates/tests/tests_td.yml` depuis le dépôt du cours
2. Créer `.github/workflows/tests_td.yml` dans leur repo personnel en collant le contenu
   (GitHub crée automatiquement les dossiers `.github/` et `workflows/`)
3. Message de commit : `Add GitHub Actions workflow`
4. À partir du TD03 : push sur `dev_tdXX` → Actions se déclenche automatiquement

**Infographies TD02 — plan complet (toutes générées) :**
- 01 — Qu'est-ce que GitHub
- 02 — Créer son compte GitHub (inscription, username, plan Free, tour de l'interface)
- 03 — Créer et explorer un dépôt (`upjv-python-datascience`)
- 04 — Rédiger son README (syntaxe Markdown + template étudiant)
- 05 — Déposer le notebook TD01 sur GitHub
- 06 — Modifier le contenu d'un dépôt (créer / uploader / dossier / modifier / supprimer)
- 07 — Utilisation des branches (créer, branche par défaut, changer)
- 08 — Accès au dépôt et collaborateurs (dépôts privés, ajouter un collaborateur)
- 09 — Token d'accès personnel (PAT)
- 10 — Cloner et dupliquer un dépôt (clone, fork)
- 11 — Issues GitHub (créer, assigner, labels, milestone)
- 12 — Pull Requests (créer, base/compare, reviewer, workflow 6 étapes)
- 13 — Examiner une Pull Request (Files changed, 3 options, merge, delete branch)
- 14 — Workflow complet TD03→TD10 (4 phases, 10 étapes, feuille de présence + quiz)

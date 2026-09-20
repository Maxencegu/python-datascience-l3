1. Architecture cible
1.1 Les quatre outils
Outil	Fonction
GitHub	Supports, dépôts étudiants, historique, projets
Google Colab	Exécution des notebooks, commandes shell, commandes Git (git pré-installé)
Google Forms	Présence, quiz, recueil des identités et liens GitHub
GitHub Actions	Exécution automatique des tests
Google Sheets	Tableau de suivi centralisé des réponses Forms
Google Drive	Données volumineuses et corrigés non encore publiés

Google Forms peut être configuré comme quiz, attribuer des points, enregistrer les réponses et fournir un retour automatique.

Google Colab et Git

Git est pré-installé dans l'environnement Colab. Les étudiants n'ont besoin d'aucune installation locale.

Ce qui fonctionne entièrement dans Colab :

!git --version         → vérifier la version de Git
!git clone <url>       → cloner un dépôt public
!git status            → voir l'état du dépôt
!git add .             → préparer les fichiers
!git commit -m "..."   → commiter
!git log               → consulter l'historique
!git diff              → voir les différences
%cd dossier            → naviguer dans les répertoires (persistant)
!ls / !pwd             → commandes shell courantes

Pour pousser vers GitHub depuis Colab, deux options :

Option A (débutants) : Fichier → Enregistrer une copie dans GitHub (OAuth automatique, sans token).
Option B (avancés, TD3+) : token GitHub stocké dans les Secrets Colab (panneau 🔑), puis git remote set-url avec le token.

La seule chose que Colab ne remplace pas : l'interface GitHub.com pour créer le dépôt depuis le modèle, consulter l'onglet Actions et lire les résultats des tests.

Persistance des données dans Colab

Colab est un environnement éphémère. Tout le contenu de /content est supprimé dans les cas suivants :

inactivité de 90 minutes ;
session dépassant 12 heures (compte gratuit) ;
fermeture du navigateur.

Ce qui disparaît : fichiers créés, dépôts clonés, packages installés.
Ce qui persiste : le notebook s'il est enregistré sur Drive ou GitHub, et les fichiers sauvegardés dans Google Drive (/content/drive/MyDrive/).

Conséquence directe : le push GitHub en fin de séance n'est pas optionnel.
C'est la seule sauvegarde réelle du travail de l'étudiant.

Workflow à enseigner dès TD1 :

Début de session    → ouvrir le notebook depuis GitHub (badge Open in Colab)
Pendant la séance   → travailler dans Colab
Fin de séance       → commit + push vers GitHub AVANT la déconnexion

La cellule setup en début de notebook (qui recrée l'environnement) est indispensable précisément parce que Colab repart de zéro à chaque session.

Options de push selon le niveau des étudiants :

Débutants (TD1-TD2) : Fichier → Enregistrer une copie dans GitHub (OAuth automatique, sans commande)

Intermédiaires (TD3+) : cellule de remise en bas du notebook :

# @title 📤 Remettre le TD sur GitHub (exécuter en fin de séance)
import subprocess
subprocess.run(["git", "add", "."])
subprocess.run(["git", "commit", "-m", "td03: completer les exercices"])
subprocess.run(["git", "push"])

Avancés (fin de semestre) : commandes git directes dans une cellule shell.

1.2 Les dépôts GitHub

Année 1 (2026-2027) — dépôt unique sous compte personnel

Le cours est hébergé dans un seul dépôt public :

Maxencegu/python-datascience

Cette approche simplifie la gestion pour la première année et suffit pour les besoins immédiats.

À partir de l’année 2 (2027-2028) — organisation GitHub

Créez une organisation GitHub, par exemple :

upjv-python-data

Elle contiendra alors :

upjv-python-data/
├── portail-cours
├── cours-commun-2026-2027
├── cours-l3-2027-2028
├── cours-m1-2027-2028
├── modele-depot-etudiant
├── modele-projet-groupe
└── outils-enseignant
Rôle de chaque dépôt

portail-cours

Page d’accueil commune :

calendrier ;
consignes ;
liens vers les TD ;
liens vers les formulaires ;
règles de remise ;
FAQ ;
barème ;
procédure de dépannage.

cours-commun-2026-2027

Contenu identique de la première année :

notebooks d’énoncé ;
données légères ;
fiches pratiques ;
liens Colab ;
corrigés publiés progressivement.

cours-l3-2027-2028 et cours-m1-2027-2028

Deux dépôts distincts à partir de l’année suivante.

modele-depot-etudiant

Dépôt modèle que chaque étudiant reproduit dans son compte.

modele-projet-groupe

Structure standard des projets en binôme ou trinôme.

outils-enseignant

Vos scripts privés :

récupération des dépôts ;
correction avec tests cachés ;
production des résultats ;
détection des fichiers absents ;
génération d’un tableau CSV.

GitHub permet de gérer des équipes et des permissions dans une organisation.

2. Décisions à prendre avant de construire

Fixez ces règles une fois pour toutes.

2.1 Comptes obligatoires

Chaque étudiant doit posséder :

un compte Google, pour Colab et éventuellement Forms ;
un compte GitHub ;
un navigateur récent ;
aucune installation Python obligatoire.

Attention : une question de type importation de fichier dans Google Forms impose une connexion à un compte Google. Puisque vous utiliserez GitHub pour les rendus, évitez l’import de fichiers dans Forms : demandez uniquement des textes, des réponses et des URL.

2.2 Dépôts publics ou privés
Solution la plus simple : dépôts étudiants publics

Avantages :

vous pouvez les consulter sans invitation ;
les Actions sont gratuites avec les runners standards dans les dépôts publics ;
les étudiants peuvent facilement fournir leur URL.

Inconvénients :

les travaux sont visibles ;
la copie entre étudiants est plus facile ;
les données utilisées doivent être publiables ;
les noms réels ne doivent pas être exigés dans le nom du dépôt.
Recommandation

Pour les TD formatifs :

dépôts publics + pseudonyme ou identifiant étudiant

Pour les projets notés :

dépôt public seulement avec l’accord explicite des étudiants ;
sinon dépôt privé et invitation de votre compte comme collaborateur ;
aucune donnée personnelle ou confidentielle dans les dépôts.

Les dépôts privés disposent d’un quota de minutes GitHub Actions selon le forfait du propriétaire. Il faudra donc surveiller la consommation si chaque étudiant utilise un dépôt privé.

2.3 Modalité de remise

Une remise est considérée comme terminée lorsque :

les fichiers sont poussés dans GitHub ;
le dernier commit est antérieur à l’échéance ;
GitHub Actions a été exécuté ;
le lien du dépôt a été enregistré dans le formulaire d’inscription initial.

L’étudiant ne doit pas envoyer le lien à chaque TD. Vous l’enregistrez une seule fois au début du semestre.

3. Structure du dépôt enseignant

Structure effective du dépôt Maxencegu/python-datascience :

python-datascience/
├── README.md
├── .gitignore
├── LICENSE
│
├── .github/
│   └── workflows/
│       └── tests.yml          ← à créer (voir section 6)
│
├── assets/
│   ├── banner.png
│   └── images/
│
├── assignments/               ← notebooks d’énoncé par TD
│   ├── td01/
│   │   ├── README.md
│   │   └── td01_enonce.ipynb
│   ├── td02/
│   │   ├── README.md
│   │   ├── td02_enonce.ipynb
│   │   └── data/
│   ├── td03/ … td09/
│   ├── mp1/
│   │   ├── README.md
│   │   └── mp1_enonce.ipynb
│   └── mp2/
│       ├── README.md
│       └── mp2_enonce.ipynb
│
├── datasets/                  ← jeux de données légers partagés
│
├── docs/                      ← documentation technique et pédagogique
│   ├── aide_colab.md
│   ├── aide_git.md
│   ├── aide_github.md
│   └── erreurs_frequentes.md
│
├── faq/                       ← questions fréquentes étudiants
│   └── faq.md
│
├── projects/                  ← consignes mini-projets et projets groupe
│
├── resources/                 ← fiches mémo et ressources complémentaires
│
└── templates/                 ← modèles de fichiers (solutions.py, tests, etc.)
Les corrigés

Ne stockez pas les corrigés sur une branche privée du même dépôt public en pensant qu’ils seront invisibles. Conservez-les :

dans un dépôt privé séparé ;
ou dans votre Drive ;
puis copiez-les dans assignments/tdXX/ après l’échéance.
4. Structure du dépôt étudiant

Le dépôt modèle doit rester identique toute l’année :

python-data-etudiant/
├── README.md
├── requirements.txt
├── .gitignore
├── .github/
│   └── workflows/
│       └── tests.yml
│
├── td01/
│   └── prise-en-main.md
│
├── td02/
│   ├── td02.ipynb
│   └── solutions.py
│
├── td03/
│   ├── td03.ipynb
│   └── solutions.py
│
├── td04/
│   ├── td04.ipynb
│   └── solutions.py
│
├── ...
│
└── projet/
    ├── README.md
    ├── data/
    ├── notebooks/
    ├── src/
    └── outputs/
Pourquoi conserver .ipynb et .py ?
Le notebook sert à évaluer
la démarche ;
les explications ;
les tableaux ;
les graphiques ;
l’interprétation économique.
Le fichier Python sert à évaluer automatiquement
les fonctions ;
les types retournés ;
les dimensions ;
les calculs ;
le nettoyage ;
les cas limites.

Le notebook peut importer le fichier Python :

from solutions import calculer_moyenne, nettoyer_donnees

Ainsi, l’étudiant ne duplique pas son code.

5. Concevoir un TD compatible avec la correction automatique
5.1 Mauvaise consigne

Calculez la moyenne des salaires.

Cette consigne ne fixe ni fonction ni sortie.

5.2 Bonne consigne

Dans td05/solutions.py, complétez la fonction
calculer_salaire_moyen(df) qui doit retourner un nombre.

Fichier fourni :

import pandas as pd


def calculer_salaire_moyen(df: pd.DataFrame) -> float:
    """Retourne la moyenne de la colonne salaire."""
    raise NotImplementedError

Test automatique :

import pandas as pd

from td05.solutions import calculer_salaire_moyen


def test_calculer_salaire_moyen():
    donnees = pd.DataFrame({"salaire": [1500, 2000, 2500]})
    resultat = calculer_salaire_moyen(donnees)

    assert isinstance(resultat, (int, float))
    assert resultat == 2000
5.3 Ce qui peut être automatisé
Élément	Automatisation
Fonction présente	Oui
Résultat numérique	Oui
Colonnes d’un DataFrame	Oui
Valeurs manquantes	Oui
Dimensions	Oui
Type de résultat	Oui
Code qui s’exécute	Oui
Présence d’un graphique	Partiellement
Qualité du graphique	Non ou très partiellement
Interprétation économique	Non
Qualité de l’argumentation	Non
Originalité du projet	Non

La note finale doit donc combiner :

note automatique + correction humaine

5.4 Intégrer des infographies dans les notebooks

Chaque TD peut inclure des infographies pédagogiques affichées directement dans Colab. Les fichiers sont versionnés dans le dépôt enseignant, co-localisés avec le notebook.

Structure des fichiers :

assignments/td01/
├── td01_enonce.ipynb
└── images/
    ├── 01_nom_de_linfographie.png
    ├── 02_nom_de_linfographie.png
    └── ...

Convention de nommage : numéro d'ordre + nom descriptif en minuscules avec underscores.

Affichage dans le notebook :

Définissez une fonction helper dans une cellule de configuration en haut du notebook :

# @title ⚙️ Configuration des ressources (ne pas modifier)
from IPython.display import Image, display

BASE_URL = "https://raw.githubusercontent.com/Maxencegu/python-datascience-l3/main/assignments/td01_fondements_de_github/images/"

def afficher_infographie(nom_fichier, largeur=1300):
    display(Image(url=BASE_URL + nom_fichier, width=largeur))

Puis dans chaque cellule de cours :

# @title Infographie — Titre de la notion
afficher_infographie("01_nom_de_linfographie.png")

Règles importantes :

Pour les images (PNG) : utilisez raw.githubusercontent.com — le MIME type est correct.
Pour les PDFs : utilisez l'URL blob de GitHub (github.com/.../blob/...) et non raw, pour que le navigateur ouvre le viewer PDF plutôt que de déclencher un téléchargement.
Un PDF séparé est rarement nécessaire si l'infographie est complète : évitez la redondance.

5.5 Concevoir des exercices interactifs dans Colab

Pattern standard en trois cellules

Toute séquence d'exercice suit la même structure :

Cellule 1 — Setup (cachée, @title)
Crée l'environnement nécessaire à l'exercice (dossiers, fichiers, état initial).
L'étudiant doit l'exécuter en premier.

Cellule 2 — Exercice
Contient les instructions en commentaires et des placeholders ____ à remplacer.
____ (4 underscores) est le marqueur standard : l'étudiant remplace chaque ____ par son code.

Cellule 3 — Validation (@title ✅)
Vérifie automatiquement les résultats et affiche un retour par étape.

Placeholder ____

____ (4 underscores) est utilisé pour tout type d'exercice (shell, Git, Python).
En Python, ____ lève un NameError si l'étudiant oublie de le remplacer.
Ne jamais utiliser ___ (3 underscores) : dans IPython/Colab, ___ est une variable d'historique
(l'avant-avant-dernière sortie, '' au départ). Un trou oublié ne lèverait pas d'erreur claire.
Évitez les placeholders sur les lignes de commandes magiques IPython (voir ci-dessous).

Exercices shell — règles spécifiques

Commande	Comportement dans Colab
!cd dossier	Ne fonctionne pas : chaque ! s'exécute dans un sous-shell isolé
%cd dossier	Fonctionne : changement permanent dans la session Colab
!ls	Retourne les fichiers sur une seule ligne (difficile à parser)
!ls -1	Retourne un fichier par ligne (recommandé pour la validation)
result = !cmd	Capture la sortie dans une liste Python (nécessaire pour valider)

Règle critique : ne jamais mettre de commentaire inline après une commande magique %.
Le commentaire est interprété comme argument de la commande.

# FAUX — essaie de naviguer dans un dossier nommé "# le bon dossier"
%cd     # le bon dossier

# CORRECT — commentaire au-dessus
# Allez dans le dossier data
%cd data

Validation des exercices shell

Seules les étapes qui modifient l'état du système sont fiables à tester automatiquement :

Étape testable automatiquement	os.getcwd() pour vérifier le répertoire courant
Étape testable automatiquement	os.listdir() pour vérifier les fichiers présents (indépendant du format de ls)
Étape auto-validée visuellement	!pwd et !ls : l'étudiant voit l'output et peut se corriger lui-même

Principe de non-redondance des exercices

Deux exercices qui utilisent la même commande et produisent le même type de sortie n'apportent pas de valeur supplémentaire. Exemple : un exercice "afficher l'historique" (git log) et un exercice "trouver le message d'un commit" (git log) sont redondants — le second est absorbé par le premier. Avant d'ajouter un exercice, vérifier qu'il introduit une commande ou un concept nouveau.

Exercices Git — règles spécifiques

Git est pré-installé dans Colab. Aucune cellule de setup n'est nécessaire pour les commandes de lecture.
Capturez toujours la sortie dans une variable pour pouvoir la valider :

version_git = !git --version
print(version_git[0])

La validation vérifie que la variable existe et contient la sortie attendue :

try:
    sortie = version_git[0] if isinstance(version_git, list) and version_git else ""
    print(f"  ✅ {sortie}" if sortie.startswith("git version") else "  ❌ Commande incorrecte")
except NameError:
    print("  ❌ version_git n'est pas défini")

Pour git init (conversion d'un répertoire existant), la validation repose sur os.path.isdir(".git") :

# Setup : crée un projet existant et positionne l'étudiant dedans
import os
os.chdir("/content")
os.makedirs("mh_survey/data", exist_ok=True)
open("mh_survey/report.md", "w").write("# Rapport santé mentale")
open("mh_survey/funding.doc", "w").write("Budget")
open("mh_survey/data/survey_results.csv", "w").write("id,score\n1,7\n2,4\n")
%cd /content/mh_survey

# Exercice : l'étudiant complète ____
!____

# Validation
import os
git_existe = os.path.isdir(".git")
bon_repertoire = os.getcwd().endswith("mh_survey")
print(f"  {'✅' if bon_repertoire else '❌'} Répertoire : {os.getcwd()}")
print(f"  {'✅' if git_existe else '❌'} Dépôt Git initialisé (.git présent)")

6. Mettre en place GitHub Actions

Dans le dépôt modèle :

name: Tests automatiques

on:
  push:
  workflow_dispatch:

jobs:
  tests:
    runs-on: ubuntu-latest

    steps:
      - name: Télécharger le dépôt
        uses: actions/checkout@v4

      - name: Installer Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.12"

      - name: Installer les dépendances
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt

      - name: Lancer les tests
        run: pytest -q

requirements.txt :

numpy
pandas
matplotlib
pytest

Commencez avec peu de dépendances. Les installations longues consomment davantage de minutes et compliquent les erreurs.

6.1 Un test par TD
tests/
├── test_td02.py
├── test_td03.py
├── test_td04.py
└── ...

Ou placez les tests dans chaque dossier :

td02/
├── solutions.py
└── test_solutions.py
6.2 Deux niveaux de tests
Tests publics dans le dépôt étudiant

Ils donnent un retour immédiat :

fonction absente ;
mauvais résultat ;
erreur de syntaxe ;
mauvaise structure.
Tests cachés dans votre dépôt privé

Ils empêchent les étudiants d’écrire du code uniquement adapté aux exemples visibles.

Votre correcteur privé :

clone les dépôts étudiants ;
copie les tests cachés ;
lance pytest ;
produit un résultat ;
exporte un fichier CSV.

C’est important : GitHub Actions exécuté dans le dépôt étudiant ne peut pas protéger des tests réellement secrets si ces tests ou leur logique sont présents dans ce dépôt.

7. Organiser les Google Forms

Je recommande quatre familles de formulaires.

7.1 Formulaire d’inscription unique

À remplir au TD1 :

Nom
Prénom
Numéro étudiant
Niveau : L3 / M1
Groupe de TD
Adresse électronique
Nom d’utilisateur GitHub
URL du dépôt GitHub
Consentement aux règles d’utilisation

Ce formulaire alimente la feuille centrale :

ETUDIANTS

Colonnes :

ID | Nom | Prénom | Niveau | Groupe | GitHub | URL dépôt
7.2 Formulaire de présence par TD

Chaque formulaire contient :

Numéro étudiant
Nom
Prénom
Groupe
Code de présence
Question très courte liée au TD précédent
Fonctionnement recommandé

Au début du TD :

vous affichez un QR code ou un lien court ;
vous donnez oralement un code valable quelques minutes ;
vous fermez les réponses après environ 5 à 10 minutes ;
vous vérifiez les doublons et incohérences.

Ne considérez pas Google Forms comme une preuve infalsifiable de présence. C’est un outil d’émargement assisté qui doit rester complété par votre observation de la salle.

7.3 Quiz de fin de TD

Configuration :

mode quiz activé ;
barème automatique ;
5 à 10 questions ;
questions obligatoires ;
correction affichée après la fermeture, pas nécessairement immédiatement ;
réponses envoyées dans une feuille Google Sheets.

Un quiz de 8 questions peut contenir :

3 questions de compréhension ;
2 lectures de code ;
2 questions sur les erreurs fréquentes ;
1 question d’interprétation.
7.4 Formulaire de constitution des projets
Niveau
Nom du groupe
Membre 1
Membre 2
Membre 3 facultatif
Nom d’utilisateur GitHub de chaque membre
URL du dépôt de groupe
Sujet choisi
8. Construire la feuille de suivi centrale

Créez un classeur :

Suivi Python Data 2026-2027

Onglets :

PARAMETRES
ETUDIANTS
PRESENCES
QUIZ
GITHUB
PROJETS
NOTES
ANOMALIES
Exemple de tableau final
ID	Niveau	Prés.	Quiz	Tests TD	Projet	Total
12345	L3	8/9	14/20	17/20	15/20	…

Ne faites pas de GitHub votre registre officiel d’identité. La correspondance :

identité universitaire ↔ compte GitHub

doit être conservée dans votre feuille privée, pas publiée dans le dépôt.

9. Déroulement précis de chaque TD
Avant la séance

Vous préparez :

notebook d’énoncé ;
données ;
fonctions à compléter ;
tests publics ;
tests cachés ;
formulaire de présence ;
quiz ;
corrigé ;
lien Colab ;
solution de secours.

Vous testez le tout avec un compte étudiant fictif.

De 0 à 10 minutes : présence
Affichage du formulaire.
Saisie du code de séance.
Question de rappel.
Fermeture du formulaire.
Présentation des objectifs.
De 10 à 25 minutes : démonstration
notion principale ;
exemple court ;
manipulation guidée.
De 25 à 90 minutes : travail Colab

Les étudiants :

ouvrent le notebook ;
enregistrent leur copie ;
travaillent ;
complètent solutions.py ;
enregistrent les fichiers.
De 90 à 105 minutes : remise GitHub

Ils mettent à jour le dépôt :

directement depuis Colab vers GitHub, lorsque le workflow est maîtrisé ;
ou en téléchargeant les fichiers puis en les déposant dans GitHub ;
ou avec Git en ligne de commande à partir du moment où vous l’avez enseigné.

Ils vérifient l’onglet Actions.

De 105 à 118 minutes : quiz

Quiz individuel de 8 à 12 minutes.

De 118 à 120 minutes : clôture
échéance exacte ;
annonce du corrigé ;
point sur le TD suivant.
10. Contenu des TD et mini-projets
Année 1 : programme commun L3/M1 (9 séances × 2h = 18h)
Séance	Contenu principal	Production GitHub
TD1	Introduction à Git	—
TD2	Introduction à GitHub	Création du dépôt et premier commit
TD3	Les bases de Python	Fonctions simples
TD4	Les fonctions, modules et NumPy	solutions.py avec fonctions NumPy
TD5	Matplotlib, dictionnaires et Pandas	Premiers graphiques et DataFrames
TD6	Logique, flux de contrôle, filtrage et boucles	Analyse guidée complète
TD7_MP1	Mini-projet 1 – Analyse exploratoire en binôme (en séance, avec quiz)	Notebook d'analyse en binôme
TD8	Pandas : agrégation et transformation des données	Analyse tabulaire avancée
Examen	Examen final individuel	—

Remarques :
- Le mini-projet MP1 est intégré en TD07 : réalisé en binôme pendant la séance, avec quiz de fin de séance comme tous les autres TD. Il n'y a plus de mini-projet à faire à la maison.
- Les étudiants qui ne finissent pas les exercices d'un TD peuvent continuer chez eux, tout doit être remis avant le TD suivant. Le quiz doit obligatoirement être fait en séance.
- Les contenus retirés (Pandas filtrage, jointures, séries temporelles, MP2) constituent la suite naturelle du programme de M1 pour les étudiants ayant suivi ce cours en L3. Le programme L3 est conçu comme un prérequis explicite du programme M1.
À partir de l’année suivante
L3
TD	Sujet
1	GitHub et Colab
2	Fondamentaux Python
3	Fonctions et collections
4	NumPy
5	Pandas : bases
6	Nettoyage et agrégation
7	Matplotlib
8	Analyse guidée
9	Mini-projet et synthèse
M1
TD	Sujet
1	Révision Git/Python et diagnostic
2	Python structuré et qualité
3	Pandas avancé
4	Échantillonnage
5	Tests statistiques
6	ANOVA et interprétation
7	Seaborn et communication
8	Analyse reproductible
9	Projet, revue et soutenance

Je recommande deux dépôts distincts, plutôt que deux branches L3 et M1. Les branches seraient source de confusion pour des étudiants débutants.

11. Organisation des projets en groupe
11.1 Dépôt par groupe
projet-nom-du-groupe/
├── README.md
├── requirements.txt
├── data/
│   ├── README.md
│   └── data_sample.csv
├── notebooks/
│   ├── 01_exploration.ipynb
│   └── 02_analyse_finale.ipynb
├── src/
│   ├── nettoyage.py
│   ├── analyse.py
│   └── visualisation.py
├── outputs/
│   ├── figures/
│   └── tables/
├── tests/
└── rapport/
11.2 Règles de collaboration

Chaque membre doit :

appartenir au dépôt ;
produire des commits identifiables ;
contribuer à au moins une partie documentée ;
participer à la présentation ;
expliquer une partie du code.

Attention : le nombre de commits ne mesure pas directement la qualité du travail. Il sert seulement d’indice pour accompagner l’évaluation collective.

11.3 Jalons
Jalon 1 — Constitution du groupe
membres ;
sujet ;
dépôt créé ;
README initial.
Jalon 2 — Données et question
source des données ;
problématique économique ;
dictionnaire des variables ;
contraintes juridiques.
Jalon 3 — Première analyse
importation ;
nettoyage ;
statistiques descriptives ;
premières visualisations.
Jalon 4 — Version finale
notebook exécutable ;
modules Python ;
résultats ;
interprétation ;
README ;
soutenance.
11.4 Barème possible
Critère	Points
Problématique économique	3
Données et traçabilité	2
Nettoyage et préparation	3
Analyse Python	4
Visualisations	2
Interprétation économique	3
Reproductibilité du dépôt	2
Organisation du groupe	1
Total	20

Les tests automatiques contrôlent surtout la reproductibilité et certains résultats. Ils ne doivent pas déterminer seuls la note.

12. Gestion des corrections
Après chaque TD
Exporter les réponses de présence.
Exporter les résultats du quiz.
Vérifier les dépôts signalés en erreur.
Exécuter les tests cachés.
Identifier les difficultés communes.
Publier le corrigé après l’échéance.
Ajouter une courte synthèse des erreurs fréquentes.
Publication du corrigé

Structure recommandée :

corrections/
└── td05/
    ├── td05_correction.ipynb
    ├── solutions.py
    └── explications.md

Le corrigé doit expliquer :

la solution ;
au moins une alternative correcte ;
les erreurs fréquentes ;
les choix de méthode ;
l’interprétation économique.
13. Sécurité et prévention des erreurs
Ne jamais placer dans un dépôt public
liste nominative des étudiants ;
notes ;
adresses électroniques ;
numéros étudiants ;
réponses individuelles ;
clés API ;
données confidentielles ;
corrigés avant l’échéance.
Ajoutez un .gitignore
__pycache__/
.pytest_cache/
.ipynb_checkpoints/
.env
*.pyc
.DS_Store
Limitez les Actions

Ajoutez un délai maximal :

timeout-minutes: 10

Évitez que les workflows soient lancés sur chaque modification inutile. Vous pouvez utiliser :

on:
  push:
    paths:
      - "td*/**"
      - "tests/**"
      - "requirements.txt"

Les limites GitHub Actions peuvent évoluer et un workflow peut être annulé lorsqu’une limite est atteinte.

14. Tests avant le lancement

Créez trois comptes ou profils de simulation :

étudiant Windows ;
étudiant macOS ;
étudiant Linux.

Comme tout passe essentiellement par le navigateur, il n’est pas nécessaire de posséder les trois systèmes physiques. Il faut néanmoins essayer Chrome, Firefox ou Edge et tester au moins les scénarios suivants.

Scénarios obligatoires
Inscription
formulaire accessible ;
adresse et identifiant enregistrés ;
URL GitHub valide.
Colab
notebook ouvert depuis GitHub ;
copie enregistrée dans Drive ;
données chargées ;
cellules exécutées.
GitHub
dépôt créé depuis le modèle ;
fichier modifié ;
commit visible ;
historique lisible.
Actions
test réussi ;
test volontairement échoué ;
message d’erreur compréhensible ;
dépendances correctement installées.
Quiz
réponse enregistrée ;
notation correcte ;
doublons repérables ;
export vers Sheets fonctionnel.
Projet
deux collaborateurs ;
contributions visibles ;
notebook exécutable depuis un compte différent.
15. Plan de mise en œuvre
Phase 1 — Fondations
créer une adresse Google dédiée au cours ;
créer ou nettoyer votre compte GitHub enseignant ;
créer l’organisation GitHub ;
activer l’authentification à deux facteurs ;
créer le Drive du cours ;
créer le classeur central ;
arrêter les règles de nommage.
Phase 2 — Squelette GitHub
créer portail-cours ;
créer cours-commun-2026-2027 ;
créer modele-depot-etudiant ;
créer modele-projet-groupe ;
créer outils-enseignant en privé ;
préparer les README ;
définir les licences et règles de confidentialité.
Phase 3 — Prototype d’un TD

Ne créez pas les neuf TD immédiatement.

Construisez entièrement le TD2 :

notebook ;
fichier solutions.py ;
tests publics ;
tests cachés ;
Action ;
formulaire de présence ;
quiz ;
corrigé ;
feuille de suivi.

Puis simulez tout le parcours.

Phase 4 — TD1 d’onboarding

Préparez un TD1 entièrement consacré au workflow :

créer les comptes ;
configurer le profil GitHub ;
créer le dépôt depuis le modèle ;
remplir le formulaire d’inscription ;
ouvrir un notebook Colab ;
modifier une fonction ;
récupérer ou enregistrer le fichier ;
pousser dans GitHub ;
lire le résultat d’une Action ;
corriger un test rouge ;
obtenir un test vert.

Le TD1 doit aboutir à une validation concrète :

Compte GitHub créé
Dépôt créé
Lien enregistré
Premier commit effectué
Action réussie
Quiz terminé
Phase 5 — Industrialisation

Une fois le prototype validé :

dupliquer la structure pour TD3 à TD9 ;
adapter les tests ;
créer les huit autres formulaires de présence ;
créer les huit autres quiz ;
préparer les corrigés ;
compléter le calendrier ;
vérifier tous les liens.
Phase 6 — Projet
créer le modèle de projet ;
définir les sujets ;
publier le barème ;
créer le formulaire des groupes ;
fixer les jalons ;
préparer une grille de soutenance ;
préparer les tests de reproductibilité.
Phase 7 — Pilote

Faites tester le système par deux ou trois personnes jouant le rôle d’étudiants :

une personne à l’aise ;
une personne débutante ;
une personne utilisant un autre système d’exploitation.

Consignez chaque blocage dans erreurs_frequentes.md.

Phase 8 — Mise en production

Avant la première séance, vérifiez :

tous les liens ;
droits d’accès ;
formulaires publiés ;
dépôts modèles accessibles ;
Actions fonctionnelles ;
datasets accessibles ;
corrigés encore privés ;
solution de secours disponible.
16. Solution de secours indispensable

Le jour d’un TD, GitHub, Colab ou Google peut être temporairement indisponible. Préparez pour chaque séance :

notebook .ipynb téléchargeable ;
données dans une archive ZIP ;
version PDF de l’énoncé ;
quiz de secours sous forme de document ;
délai de remise alternatif annoncé à l’avance.

Une panne d’un service ne doit pas pénaliser un étudiant.

17. Ce qu’il faut préparer concrètement

Votre lot initial comprend :

1 organisation GitHub
5 à 7 dépôts structurants
1 portail étudiant
1 modèle de dépôt individuel
1 modèle de dépôt de groupe
9 notebooks d’énoncé
8 notebooks Python/Data Science + TD1 Git
8 ou 9 fichiers solutions.py
8 jeux de tests publics
8 jeux de tests cachés
9 formulaires de présence
9 quiz
1 formulaire d’inscription
1 formulaire de groupes
1 classeur de suivi
1 guide étudiant
1 guide enseignant
1 FAQ
1 procédure de secours
1 grille de projet
1 grille de soutenance
18. État d'avancement (mis à jour 2026-07-19)

Séance	Statut	Notes
TD1	✅ Terminé	8 infographies PNG dark (01-08), notebook complet avec badge Open in Colab, poussé sur GitHub
TD2	⏳ À faire	Python bases + listes (contenu GitHub cours à adapter)
TD3–TD9	🔲 Non commencé	—
MP1, MP2	🔲 Non commencé	—

Détails TD1 :
- Infographies : 8 fichiers *_pro.png, 1200×2px (2x DPI), thème sombre, viewport 1200px
- Exercices : shell (pwd/cd/ls), git init, staging, commit, log (limité, par fichier, par date), diff (staged, entre commits), QCM diff, unstage (git restore --staged), revert (git revert HEAD --no-edit)
- Notebook : 72 cellules, badge Open in Colab en cellule 0

19. Ordre de travail recommandé

Ne cherchez pas à tout produire dans le désordre. Suivez cet ordre :

règles pédagogiques et barème ;
architecture des dépôts ;
modèle étudiant ;
prototype complet du TD2 ;
GitHub Actions ;
tableau de suivi ;
TD1 Git/GitHub ;
modèle de projet ;
autres TD ;
tests pilotes ;
publication.

Le premier objectif opérationnel n’est pas de préparer neuf notebooks. C’est de réussir intégralement ce scénario :

Un faux étudiant s’inscrit
→ crée son dépôt
→ ouvre un notebook dans Colab
→ complète une fonction
→ remet son code dans GitHub
→ déclenche GitHub Actions
→ obtient un retour
→ répond au quiz
→ apparaît correctement dans votre suivi
# \# 🏠 Analyse des Prix Airbnb à Paris

# 

# \## 📋 Contexte

# Analyse exploratoire complète du marché Airbnb parisien basée sur \*\*81 853\*\* logements réels (données Inside Airbnb, 2024). Le projet inclut un pipeline de nettoyage de données de bout en bout et une analyse statistique descriptive des facteurs influençant les prix.

# 

# \## ❓ Questions analysées

# 1\. Quels arrondissements ont les prix les plus élevés ?

# 2\. Quelle est la distribution des types de logements à Paris ?

# 3\. Quelles sont les caractéristiques globales du parc immobilier disponible (chambres, notes, disponibilités) ?

# 

# \## 📊 Résultats clés

# \- \*\*Volume global :\*\* Un dataset massif de \*\*81 853 lignes\*\* analysées après pipeline de nettoyage.

# \- \*\*Typologie dominante :\*\* Les données révèlent une écrasante majorité de locations de \*\*logements entiers\*\* (\*Entire home/apt\*) par rapport aux chambres privées.

# \- \*\*Satisfaction :\*\* Une distribution des notes voyageurs (\*review\_scores\_rating\*) fortement concentrée vers le haut, frôlant une médiane globale de \*\*4.5/5\*\*.

# 

# \## 🖼️ Aperçus

# 

# \### 1. Prix médian par arrondissement (Top 15)

# !\[Prix par quartier](outputs/q1\_prix\_par\_quartier.png)

# 

# \### 2. Rapport d'analyse automatisé (Sweetviz)

# Le pipeline génère également un dashboard d'exploration interactif complet :

# \* \*\*81 853\*\* rangs analysés

# \* \*\*10\*\* caractéristiques clés (7 numériques, 2 catégorielles, 1 textuelle)

# 

# \## 🛠️ Stack technique

# \* \*\*Langage :\*\* Python

# \* \*\*Data Wrangling :\*\* Pandas, Numpy

# \* \*\*Visualisation :\*\* Matplotlib, Seaborn

# \* \*\*Exploratoire Automatisé :\*\* Sweetviz

# \* \*\*Versionning :\*\* Git

# 

# \## 🚀 Lancer le projet

# 

# ```bash

# \# 1. Cloner le projet

# git clone \[https://github.com/TON-PSEUDO/-airbnb-paris-eda-](https://github.com/TON-PSEUDO/-airbnb-paris-eda-)

# cd -airbnb-paris-eda-

# 

# \# 2. Installer les packages requis

# pip install -r requirements.txt

# 

# \# 3. Exécuter le pipeline de nettoyage des données

# python src/cleaning.py

# 

# \# 4. Générer le rapport d'analyse exploratoire Sweetviz

# python "src/rapport\_ sweetviz.py"

# 

# \# 5. Ouvrir le Notebook d'analyse pour voir les graphiques

# jupyter notebook notebooks/02\_analyse.ipynb


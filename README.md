# Python pour la data-science: Prédiction Nvidia

MODIFIER : 
- cadre
- Sujet
-   Introduction et context rapide : catch moment 
-   Problématisation du projet : qst problématsée concrète
-   Reexplication de la qst -> preshot un plan
-   Plan global
-   Dire que ya le guide de lecture (sommaire global dans le fichier main) 
- choix sujet et motivation

- redirection vers rEADME 2 (technique)

Ce projet a été réalisé par Joël Khayat, Kenan Darfilali et Massil Zouaghi dans le cadre du cours Python pour la Data Science, dispensé par Lino Galiana. Ce travail s'inscrit dans une démarche d'application des outils de manipulation de données et de Machine Learning à des problématiques réelles des marchés financiers.


1/ Choix du sujet et motivation

Le choix de porter notre analyse sur le secteur boursier, et plus spécifiquement sur NVIDIA, est né de la convergence entre nos intérêts personnels pour les nouvelles technologies et les enjeux économiques actuels. En tant que passionnés de tech et de culture geek, nous avons été les témoins directs de l'hégémonie de NVIDIA, passant de leader des cartes graphiques pour le jeu vidéo à pilier indispensable de l'infrastructure mondiale de l'intelligence artificielle.

L'évolution du titre sur les dix dernières années est sans précédent : NVIDIA n'est plus seulement une entreprise de semi-conducteurs, c'est devenu l'épicentre d'une révolution technologique. Étudier la dynamique de son action nous permet de lier notre affinité technique pour leurs produits à une analyse rigoureuse de la donnée financière.

2/ Problématique

L'objectif central de ce projet est de modéliser la liquidité de l'action NVIDIA en cherchant à prédire son volume quotidien de transactions.

3/ Méthodologie et démarche scientifique

Pour répondre à cette problématique, nous avons structuré notre recherche autour d'un pipeline de données complet. La première étape a consisté en une phase de collecte multi-sources automatisée. Cette approche nous a permis d'analyser l'action au sein de son écosystème global. Une fois les données nettoyées et les indicateurs techniques calculés (rendements, volatilité, moyennes mobiles), nous avons mis en concurrence trois modèles d'apprentissage supervisé pour le forecasting du volume : les arbres de décision, les forêts aléatoires et le gradient boosting via XGBoost.

4/Guide de reproduction

Prérequis (Packages nécessaires)
Pour exécuter les notebooks, vous devez disposer d'un environnement Python 3 avec les bibliothèques suivantes installées :
Data : pandas, numpy, pathlib
Finance : yfinance, pandas-datareader
Visualisation : matplotlib, seaborn
Machine Learning : scikit-learn, xgboost


Instructions d'exécution
NoteBook.ipynb : Ce fichier doit être exécuté en premier. Il gère l'importation en temps réel des données via les APIs de Yahoo Finance et de la FRED. Il contient également l'entraînement des modèles de prédiction de volume.


5/ Résultats et conclusion

Nos analyses mettent en évidence une corrélation extrêmement forte entre les ruptures technologiques majeures et les volumes d'échanges sur le titre NVDA. Sur le plan prédictif, le modèle XGBoost s'est révélé être le plus performant pour anticiper les dynamiques de marché, surpassant les modèles plus simples grâce à sa gestion fine des non-linéarités. En conclusion, ce projet démontre que si la croissance de NVIDIA semble portée par l'innovation, son activité de marché reste intrinsèquement liée à des variables macro-économiques et à une volatilité sectorielle qui exigent une modélisation complexe.

6/ Apport du projet et apprentissages

Ce travail nous a permis de consolider nos compétences en Python, notamment sur l'automatisation de la récupération de données massives et l'implémentation de modèles de régression robustes. Au-delà de l'aspect technique, il nous a appris à transformer une intuition (le succès de NVIDIA) en une étude quantitative documentée. Ce projet sert de base à la compréhension de la valorisation des actifs technologiques de growth et illustre comment les outils de la Data Science peuvent éclairer l'étude des comportements de marché.

7/ Structure du dépôt Git

NoteBook.ipynb : Coeur du travail (importation, traitement, analyse descriptive et modèles de prédiction).

Final copy.ipynb : Synthèse consolidée et interprétations financières.

nvda_stock_data.csv : Données de marché de l'action NVIDIA extraites pour la période du 01-01-2015 au 01-01-2024 (données intermédiaires de référence).

Merci pour votre lecture !



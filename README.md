# Python pour la data-science: Prédiction Nvidia

Ce projet a été réalisé par Joël Khayat, Kenan Darfilali et Massil Zouaghi dans le cadre du cours "Python pour la Data Science", dispensé par Lino Galiana. Ce travail s'inscrit dans une démarche d'application des outils de manipulation de données et de Machine Learning à des problématiques réelles des marchés financiers.

1/Choix du sujet et motivation

Le choix de porter notre analyse sur le secteur boursier, et plus spécifiquement sur NVIDIA, est né de la convergence entre nos intérêts personnels pour les nouvelles technologies et les enjeux économiques actuels. En tant que passionnés de tech et de culture "geek", nous avons été les témoins directs de l'hégémonie de NVIDIA, passant de leader des cartes graphiques pour le jeu vidéo à pilier indispensable de l'infrastructure mondiale de l'intelligence artificielle.

L'évolution du titre sur les dix dernières années est sans précédent : NVIDIA n'est plus seulement une entreprise de semi-conducteurs, c'est devenu l'épicentre d'une révolution technologique. Étudier la dynamique de son action nous permet de lier notre affinité technique pour leurs produits à une analyse rigoureuse de la donnée financière.

2/Problématique

L'objectif central de ce projet est de modéliser la liquidité de l'action NVIDIA en cherchant à prédire son volume quotidien de transactions.

3/Méthodologie et démarche scientifique

Pour répondre à cette problématique, nous avons structuré notre recherche autour d'un pipeline de données complet. La première étape a consisté en une phase de collecte multi-sources automatisée. Cette approche nous a permis d'analyser l'action au sein de son écosystème global. Une fois les données nettoyées et les indicateurs techniques calculés (rendements, volatilité, moyennes mobiles), nous avons mis en concurrence trois modèles d'apprentissage supervisé pour le forecasting du volume : les arbres de décision, les forêts aléatoires et le gradient boosting via XGBoost.

4/Résultats et conclusion

Nos analyses mettent en évidence une corrélation extrêmement forte entre les ruptures technologiques majeures et les volumes d'échanges sur le titre NVDA. Sur le plan prédictif, le modèle XGBoost s'est révélé être le plus performant pour anticiper les dynamiques de marché, surpassant les modèles plus simples grâce à sa gestion fine des non-linéarités. En conclusion, ce projet démontre que si la croissance de NVIDIA semble portée par l'innovation, son activité de marché reste intrinsèquement liée à des variables macro-économiques et à une volatilité sectorielle qui exigent une modélisation complexe.

5/Apport du projet et apprentissages

Ce travail nous a permis de consolider nos compétences en Python, notamment sur l'automatisation de la récupération de données massives et l'implémentation de modèles de régression robustes. Au-delà de l'aspect technique, il nous a appris à transformer une intuition (le succès de NVIDIA) en une étude quantitative documentée. Ce projet sert de base à la compréhension de la valorisation des actifs technologiques de "growth" et illustre comment les outils de la Data Science peuvent éclairer l'étude des comportements de marché.

6/Structure du dépôt Git

L'intégralité de l'analyse est répartie dans les fichiers suivants :

NoteBook.ipynb : Coeur du travail qui contient l'importation des données ainsi que leur traitement, une analyse descriptive de ces dernières ainsi que les modèles de prédiction de volume d'actions échangés.
nvda_stock_data.csv: Données de marché de l'action NVIDIA sur la période que nous avons choisi, à savoir du 01-01-2015 au 01-01-2024

 Merci pour votre lecture !



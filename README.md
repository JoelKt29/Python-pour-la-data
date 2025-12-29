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



























1. Introduction
L’objectif est d’exploiter des données de marché afin d’étudier l’évolution du cours de l’action, d’en extraire des indicateurs pertinents et d’en proposer une interprétation économique et financière.

2. Présentation de l’entreprise
NVIDIA est une entreprise technologique américaine spécialisée dans la conception de processeurs graphiques (GPU) et de solutions de calcul haute performance. Historiquement positionnée sur les cartes graphiques pour le jeu vidéo, l’entreprise occupe aujourd’hui une place centrale dans les domaines de l’intelligence artificielle, du calcul intensif et des centres de données.

Cette position stratégique explique l’intérêt particulier porté à son cours boursier, notamment dans un contexte de forte croissance liée au développement de l’IA.

3. Données et méthodologie
Les données utilisées dans le notebook proviennent de sources financières accessibles via des bibliothèques Python dédiées. Elles portent principalement sur : les prix de l’action NVIDIA (ouverture, clôture, plus hauts et plus bas), les volumes échangés, une période suffisamment longue pour analyser les tendances.

Le traitement des données repose sur les bibliothèques standards (pandas, numpy, matplotlib, etc.). 

Les différentes étapes comprennent : le chargement et le nettoyage des données, la construction de séries temporelles, le calcul d’indicateurs descriptifs, la visualisation graphique.

4. Analyse descriptive du cours de l’action
Le notebook met en évidence une forte dynamique haussière du cours de l’action NVIDIA sur la période étudiée. Les graphiques de prix montrent : une tendance de long terme clairement positive, des phases de correction ponctuelles, une volatilité non négligeable, caractéristique des valeurs technologiques.
L’évolution des volumes confirme l’intérêt croissant des investisseurs, avec des pics correspondant à des annonces majeures ou à des phases d’anticipation de résultats financiers.

5. Indicateurs financiers et interprétation
Plusieurs indicateurs sont calculés et analysés dans le notebook, notamment : des rendements journaliers, des moyennes mobiles, des mesures de volatilité. Les rendements mettent en évidence des périodes de forte performance, mais également des épisodes de corrections rapides. Les moyennes mobiles permettent d’identifier les tendances et les points de retournement potentiels, tandis que la volatilité reflète l’incertitude associée aux perspectives de croissance de l’entreprise.

6. Discussion économique
Les résultats observés sont cohérents avec le contexte économique et sectoriel de NVIDIA. La montée en puissance de l’intelligence artificielle et des besoins en calcul intensif a renforcé les anticipations de croissance, ce qui se reflète dans la valorisation boursière.

Cependant, cette valorisation élevée s’accompagne de risques : dépendance à l’innovation technologique, cyclicité du secteur, sensibilité aux conditions macroéconomiques et financières.

# Projet Python (2A ENSAE) - Comment NVIDIA a explosé entre 2015 et 2024 : Étude statistique et modélisation de sa performance boursière par des méthodes de prévision.

## Cadre du projet
Projet réalisé dans le cadre pédagogique du cours de Python pour Data Science de 2A à l’ENSAE, encadré par Lino Galiana.
Membres du groupe : Kenan Darfilali, Joël Khayat et Massil Zouaghi. 

## Présentation du sujet
Sur la dernière décennie, NVIDIA (NVDA) est devenue une entreprise centrale dans l’écosystème des semi-conducteurs, notamment via les GPU utilisés en data centers et pour des usages liés à l’IA. Cette montée en puissance s’est reflétée en bourse : le titre a connu des phases de croissance rapides, mais aussi des périodes de forte volatilité.

Cette ascension fulgurante nous a poussés à vouloir l’étudier de plus près afin de mieux comprendre comment elle s’est opérée. Pour ce faire, nous avons choisi ce sujet et formulé la problématique suivante : 
> Comment quantifier la montée en puissance de NVIDIA et, dans cette optique, prévoir le volume de transactions du titre à l’instant t+1 à partir des informations disponibles jusqu’à t ?

## Méthodologie et plan 
Pour ce faire, nous avons suivi un plan en trois parties :

- Récupération des données
- Visualisation des données
- Modélisation

L’idée du projet étant d’étudier l’action NVDA à travers son activité de marché (volume), nous avons naturellement récupéré ses données de prix et de volume via **Yahoo Finance**.

Mais l’enjeu est aussi de replacer NVDA dans son environnement de marché. Nous avons donc importé plusieurs séries de référence afin d’enrichir l’analyse :

- Marché global** : SPY
- **Technologie** : QQQ
- **Semi-conducteurs** : SOXX
- **Régime de risque** : VIX
- **Conditions financières** : taux US à 10 ans

Enfin, le projet met un point d’attention sur la reproductibilité : stockage local des données brutes et traitées, pipeline rejouable, et évaluation cohérente en séries temporelles.

## Structure du projet et conseils de navigation

Le dépôt s’articule autour d’un notebook principal : **`Main_NoteBook.ipynb`**.

Le dossier **`data/`** contient une sauvegarde des données utilisées au moment du dépôt. En effet, si les politiques d’accès aux données ou les formats changent, cela peut casser le projet ; nous avons donc conservé un **backup**.

* **`data/processed/`** : bases nettoyées et préparées
* **`data/raw/`** : bases brutes (telles que téléchargées)

- 
## Prérequis 
---

## Choix et motivation du sujet
- **Finance de marché (concret)** : le volume est une variable directement liée à l’activité, aux chocs d’information et aux régimes de risque — c’est un bon terrain pour appliquer une démarche “data science” sur des séries financières.
- **NVIDIA est un cas d’étude riche** : croissance marquée, phases de stress, forte sensibilité au secteur semi-conducteurs et à la tech, et actualité structurée par l’IA. 
- **Dimension “macro + géopolitique”** : intégrer VIX et taux 10 ans permet de contextualiser les régimes de marché, et l’arrière-plan des contrôles export / tensions techno rappelle que la dynamique d’un actif tech n’est pas seulement “micro-entreprise”. 
- **Objectif pédagogique (Python data science)** : le projet mobilise proprement les briques du cours (collecte, nettoyage, EDA, modélisation, évaluation temporelle, reproductibilité) avec un cas réaliste. 

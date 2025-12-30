# Projet Python (2A ENSAE) - Comment NVIDIA a explosé entre 2015 et 2024 : Étude statistique et modélisation de sa performance boursière par des méthodes de prévision.

## Cadre du projet
Projet réalisé dans le cadre pédagogique du cours de Python pour Data Science de 2A à l’ENSAE, encadré par Lino Galiana.
Membres du groupe : Kenan Darfilali, Joël Khayat et Massil Zouaghi. 

## Présentation du sujet
Sur la dernière décennie, NVIDIA (NVDA) est devenue une entreprise centrale dans l’écosystème des semi-conducteurs, notamment via les GPU utilisés en data centers et pour des usages liés à l’IA. Cette montée en puissance s’est reflétée en bourse : le titre a connu des phases de croissance rapides, mais aussi des périodes de forte volatilité.

Cette ascension fulgurante nous a poussés à vouloir l’étudier de plus près afin de mieux comprendre comment elle s’est opérée. Pour ce faire, nous avons choisi ce sujet et formulé la problématique suivante : 
**Comment quantifier la montée en puissance de NVIDIA et, dans cette optique, prévoir le volume de transactions du titre à l’instant t+1 à partir des informations disponibles jusqu’à t ?**

Donc l’objectif principal de ce projet est d’exploiter des techniques de **data science sur séries temporelles financières** pour analyser la montée en puissance boursière de NVIDIA (NVDA) et construire un modèle capable de **prévoir le volume de transactions à un jour d’horizon** (t+1) à partir d’informations disponibles au jour (t). En combinant des variables propres à NVDA (rendements, volatilité réalisée, inertie du volume) avec des variables de contexte (ETFs marché/tech/secteur, VIX et taux US 10 ans), nous cherchons à distinguer ce qui relève de dynamiques spécifiques au titre de ce qui s’explique par des facteurs plus systémiques. Ce travail vise ainsi à fournir une lecture reproductible et quantitative de l’évolution de NVDA, tout en évaluant rigoureusement la capacité prédictive de ces signaux dans un cadre temporel réaliste.

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

## Structure du projet

Le dépôt s’articule autour d’un notebook principal : **`Main_NoteBook.ipynb`**.

Le dossier **`data/`** contient une sauvegarde des données utilisées au moment du dépôt. En effet, si les politiques d’accès aux données ou les formats changent, cela peut casser le projet ; nous avons donc conservé un **backup**.

* **`data/processed/`** : bases nettoyées et préparées
* **`data/raw/`** : bases brutes (telles que téléchargées)

## Prérequis et conseils utilisation
Avant de commencer, nous vous conseillons de suivre les étapes suivantes. Il est conseillé également d'appliquer le code sur SSPCloud avec un environnement avec GPU pour une optimalité dans les calculs et la modélisation.

```bash
# Installation de l'environnement virtuel (à exécuter dans le terminal)
python -m pip install virtualenv
python -m virtualenv .venv

# Activation de l'environnement virtuel
source .venv/bin/activate

git clone https://github.com/JoelKt29/Python-pour-la-data
cd Python-pour-la-data

# Installation des dépendances
pip install -r requirements.txt

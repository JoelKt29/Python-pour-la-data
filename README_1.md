# Projet Python (2A ENSAE) - Comment NVIDIA a explosé entre 2015 et 2024 : Étude statistique et modélisation de sa performance boursière par des méthodes de prévision.

## Cadre du projet
Projet réalisé dans le cadre pédagogique du cours de Python pour Data Science de 2A à l’ENSAE, encadré par Lino Galiana.
Membres du groupe : Kenan Darfilali, Joël Khayat et Massil Zouaghi. 

## Présentation du sujet
Sur la dernière décennie, NVIDIA (NVDA) est devenue une entreprise centrale dans l’écosystème des semi-conducteurs, notamment via les GPU utilisés en data centers et pour des usages liés à l’IA. Cette montée en puissance s’est reflétée en bourse : le titre a connu des phases de croissance rapides, mais aussi des périodes de forte volatilité.

Cette ascension fulgurante nous a poussés à vouloir l’étudier de plus près afin de mieux comprendre comment elle s’est opérée. Pour ce faire, nous avons choisi ce sujet et formulé la problématique suivante : 
> Comment quantifier la montée en puissance de NVIDIA et, dans cette optique, prévoir le volume de transactions du titre à l’instant t+1 à partir des informations disponibles jusqu’à t ?

## Méthodologie et plan 


Dans ce contexte, un objet de marché particulièrement intéressant est le **volume de transactions** : il reflète l’intensité de l’activité (arrivées d’information, annonces, stress, rotations sectorielles, etc.). L’idée du projet est donc d’étudier le cours NVDA **à travers l’activité** (volume), en la replaçant dans son environnement :
- **Marché global** (SPY),  
- **Tech** (QQQ),  
- **Semi-conducteurs** (SOXX),  
- **Régime de risque** via le **VIX**,  
- **Conditions financières** via le **taux US 10 ans**. 

Enfin, le projet met un point d’attention sur la **reproductibilité** : stockage local des données brutes/traitées, pipeline rejouable, et évaluation cohérente en séries temporelles. 

## Structure du projet et conseils de navigation 

## Prérequis 
---

## Choix et motivation du sujet
- **Finance de marché (concret)** : le volume est une variable directement liée à l’activité, aux chocs d’information et aux régimes de risque — c’est un bon terrain pour appliquer une démarche “data science” sur des séries financières.
- **NVIDIA est un cas d’étude riche** : croissance marquée, phases de stress, forte sensibilité au secteur semi-conducteurs et à la tech, et actualité structurée par l’IA. 
- **Dimension “macro + géopolitique”** : intégrer VIX et taux 10 ans permet de contextualiser les régimes de marché, et l’arrière-plan des contrôles export / tensions techno rappelle que la dynamique d’un actif tech n’est pas seulement “micro-entreprise”. 
- **Objectif pédagogique (Python data science)** : le projet mobilise proprement les briques du cours (collecte, nettoyage, EDA, modélisation, évaluation temporelle, reproductibilité) avec un cas réaliste. 

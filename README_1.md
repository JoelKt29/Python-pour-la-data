# Projet Python (2A ENSAE) — 
## Comment NVIDIA a explosé entre 2015 et 2024 : Étude statistique et modélisation de sa performance boursière par des méthodes de prévision.
---
 

## Cadre du projet
Projet réalisé dans le cadre pédagogique du cours de Python pour Data Science de 2A à l’ENSAE, encadré par Lino Galiana.
Membres du groupe : 

---

## Titres possibles (au choix)
1. **NVDA : prédire le volume de transactions à J+1 (données marché + macro)**
2. **NVIDIA en Bourse : forecast du volume et mise en contexte marché/secteur**
3. **Volume Forecasting sur NVDA : baseline → Ridge → Random Forest → validation temporelle**
4. **Quand l’activité explose : modéliser le volume NVDA avec VIX, taux et ETFs**
5. **Trading Activity Analytics : comprendre et prédire le volume de NVDA**

---

## Présentation du sujet

### Introduction & contexte
Sur la dernière décennie, **NVIDIA (NVDA)** est devenue une entreprise centrale dans l’écosystème des semi-conducteurs, notamment via les **GPU** utilisés en **data centers** et pour des usages liés à l’IA (entraînement / inférence). Cette montée en puissance s’est reflétée en bourse : le titre a connu des phases de croissance rapides, mais aussi des périodes de forte volatilité. 

Au-delà de la dynamique “entreprise”, le dossier semi-conducteurs est aussi **géopolitique** : la disponibilité des puces et l’accès aux marchés peuvent être affectés par des **restrictions à l’export** sur certains composants avancés, et plus généralement par la structuration de la chaîne de valeur mondiale. 

Dans ce contexte, un objet de marché particulièrement intéressant est le **volume de transactions** : il reflète l’intensité de l’activité (arrivées d’information, annonces, stress, rotations sectorielles, etc.). L’idée du projet est donc d’étudier le cours NVDA **à travers l’activité** (volume), en la replaçant dans son environnement :
- **Marché global** (SPY),  
- **Tech** (QQQ),  
- **Semi-conducteurs** (SOXX),  
- **Régime de risque** via le **VIX**,  
- **Conditions financières** via le **taux US 10 ans**. 

Enfin, le projet met un point d’attention sur la **reproductibilité** : stockage local des données brutes/traitées, pipeline rejouable, et évaluation cohérente en séries temporelles. 

### Problématique (versions possibles)
1. **Problème principal (direct, “modélisation”)**  
   > *Peut-on prédire le volume de transactions de NVDA au jour \(t+1\) à partir des informations disponibles au jour \(t\) (NVDA + marché/secteur + macro) ?*

2. **Version “valeur ajoutée” (baseline vs features)**  
   > *Les variables de contexte (ETFs, VIX, taux) apportent-elles un gain mesurable pour prévoir \(Volume_{t+1}\) au-delà d’une baseline d’inertie \(Volume_t\) ?*

3. **Version “interprétation économique” (drivers de l’activité)**  
   > *Dans quelle mesure l’activité sur NVDA est-elle principalement “systématique” (marché/secteur/régime de risque) versus spécifique au titre (volatilité propre, inertie du volume, épisodes extrêmes) ?*

### Plan suivi (plan général du notebook)
- **A — Récupération, sauvegarde et fusion des données**  
  Construction d’un dataset unique (NVDA + ETFs + FRED), alignement temporel, stockage *raw/processed* pour rejouabilité.  
- **B — Analyse descriptive et visualisation**  
  Prix, rendements, volatilité réalisée, drawdowns, comparaison NVDA vs marché/secteur, corrélations sur variations.  
- **C — Modélisation : forecast du volume \(t+1\)**  
  Baseline (inertie), Ridge, Random Forest, visualisation des prédictions, interprétabilité, puis validation temporelle plus robuste (TimeSeriesSplit).

---

## Choix et motivation du sujet
- **Finance de marché (concret)** : le volume est une variable directement liée à l’activité, aux chocs d’information et aux régimes de risque — c’est un bon terrain pour appliquer une démarche “data science” sur des séries financières.
- **NVIDIA est un cas d’étude riche** : croissance marquée, phases de stress, forte sensibilité au secteur semi-conducteurs et à la tech, et actualité structurée par l’IA. 
- **Dimension “macro + géopolitique”** : intégrer VIX et taux 10 ans permet de contextualiser les régimes de marché, et l’arrière-plan des contrôles export / tensions techno rappelle que la dynamique d’un actif tech n’est pas seulement “micro-entreprise”. 
- **Objectif pédagogique (Python data science)** : le projet mobilise proprement les briques du cours (collecte, nettoyage, EDA, modélisation, évaluation temporelle, reproductibilité) avec un cas réaliste. 

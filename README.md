# Projet de Data Mining : Analyse et Prétraitement des Données

### Introduction

Ce projet a pour objectif d'effectuer une analyse exploratoire et un prétraitement des données à partir d'un ensemble de données climatiques couvrant l'algerie. L'analyse des données réelles est essentielle pour extraire des informations significatives et garantir la qualité des données avant l'application d'algorithmes de Data Mining.

### Objectifs du Projet

Le projet est divisé en deux parties principales :

1. **Analyse Exploratoire des Données (AED)** : 
   - Examen des attributs, des valeurs et des distributions.
   - Identification des problèmes potentiels tels que les valeurs aberrantes et les données manquantes.

2. **Prétraitement des Données** :
   - Nettoyage des données, intégration de sources multiples, réduction de la taille des données, et transformation par normalisation.

### Fonctionnalités de l'Application

L'application développée doit permettre les manipulations de données suivantes :

#### A. Manipulation des Données
- Importation, visualisation et sauvegarde du contenu d'un dataset.
- Description globale du dataset.
- Mise à jour et suppression d'instances ou de valeurs du dataset.

#### B. Analyse des Caractéristiques des Attributs
- Calcul des mesures de tendance centrale et déduction des symétries.
- Calcul des mesures de dispersion et identification des valeurs aberrantes.
- Calcul des valeurs manquantes et des valeurs uniques.
- Construction de boxplots pour afficher les valeurs aberrantes.
- Construction d'histogrammes pour visualiser la distribution des données.
- Construction et affichage de scatter plots pour déduire des corrélations.

#### C. Prétraitement des Données
- Réduction des données par agrégation saisonnière.
- Intégration des données : fusion de données provenant de plusieurs sources.
- Options multiples pour traiter les valeurs aberrantes et les valeurs manquantes.
- Normalisation des données : méthodes Min-Max et z-score.
- Réduction des données via la discrétisation des données continues : égalité de fréquence/amplitude.
- Réduction des données par élimination des redondances (horizontal/vertical).

### Technologies Utilisées

- **Langage de programmation** : Python
- **Bibliothèques** :
  - Pandas : pour la manipulation des données.
  - NumPy : pour les calculs numériques.
  - Matplotlib et Seaborn : pour la visualisation des données.
  - Django : pour l'interface
 

### Description des jeux de données
#### Dataset `country` (Informations géographiques et administratives)

| Attribut      | Type       | Description |
|---------------|------------|-------------|
| **AREA**      | float      | La superficie totale de la région (en km², par exemple). |
| **PERIMETER** | float      | Le périmètre de la frontière du pays ou de la région. |
| **CNT1M_1_**  | int        | Un identifiant unique (numérique) pour chaque pays ou région. |
| **CNT1M_1_ID**| int        | Un autre identifiant unique, utilisé pour indexer les entités géographiques. |
| **FAO_NAME**  | string     | Nom du pays selon la FAO (Organisation des Nations unies pour l'alimentation et l'agriculture). |
| **FAO_CODE**  | int        | Code FAO du pays (numérique). |
| **UN_CODE**   | int        | Code numérique unique attribué par l'ONU pour chaque pays. |
| **ISO_CODE**  | string     | Code ISO du pays (2 lettres). |
| **CNTRY_NAME**| string     | Nom complet du pays. |
| **ISO3_CODE** | string     | Code ISO du pays (3 lettres). |
| **geometry**  | Polygon    | Géométrie du pays (données spatiales pour le contour du pays). |

#### Dataset `soil` (Données de sol)

| Attribut                  | Type   | Description |
|---------------------------|--------|-------------|
| **CEC subsoil**           | float  | Capacité d'échange cationique dans le sous-sol (capacité du sol à retenir les nutriments). |
| **CEC clay topsoil**      | float  | Capacité d'échange cationique dans l'argile de surface. |
| **CEC Clay subsoil**      | float  | Capacité d'échange cationique dans l'argile du sous-sol. |
| **CaCO3 % topsoil**       | float  | Pourcentage de carbonate de calcium en surface (affecte le pH du sol). |
| **CaCO3 % subsoil**       | float  | Pourcentage de carbonate de calcium dans le sous-sol. |
| **BD topsoil**            | float  | Densité apparente du sol en surface (mesure de la compacité). |
| **BD subsoil**            | float  | Densité apparente du sol dans le sous-sol. |
| **C/N topsoil**           | float  | Ratio carbone/azote en surface (indicateur de fertilité). |
| **C/N subsoil**           | float  | Ratio carbone/azote dans le sous-sol. |
| **geometry**              | Polygon| Géométrie des zones de sol. |

#### Dataset `climate` (Données climatiques de pluie)

| Attribut      | Type     | Description |
|---------------|----------|-------------|
| **AREA**      | float    | Superficie de la zone couverte (peut varier en fonction de la grille des données). |
| **PERIMETER** | float    | Périmètre de la zone étudiée (ici, c’est une approximation pour chaque point). |
| **CNT1M_1_**  | int      | Identifiant unique pour chaque région étudiée dans le fichier NetCDF. |
| **CNT1M_1_ID**| int      | Autre identifiant unique pour les entités de la grille. |
| **FAO_NAME**  | string   | Nom du pays, ici en rapport avec les grilles de données. |
| **FAO_CODE**  | int      | Code FAO associé aux données géographiques. |
| **UN_CODE**   | int      | Code ONU correspondant à chaque pays, ici pour la région. |
| **ISO_CODE**  | string   | Code ISO du pays (2 lettres). |
| **CNTRY_NAME**| string   | Nom complet du pays. |
| **ISO3_CODE** | string   | Code ISO à 3 lettres. |


### Instructions

1. Clonez ce repository :
   ```bash
   git clone https://github.com/votre_nom_dutilisateur/Projet_Data_Mining.git
   ```




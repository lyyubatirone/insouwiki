# Architecture des données d'InsouWiki

## Principe général

InsouWiki repose sur un registre documentaire versionné.

Le moteur distingue :

- les sources ;
- les documents ;
- les versions de documents ;
- les transcriptions ;
- les analyses ;
- les publications.

Un document est une identité stable.
Une version est un état observé de ce document à une date donnée.

## Entités principales

### Source

Une source représente un point d'origine documentaire.

Exemples :

- une chaîne YouTube ;
- un blog personnel ;
- un site institutionnel ;
- une page officielle ;
- un dépôt de documents.

Champs principaux :

- identifiant technique ;
- identifiant permanent ;
- type de source ;
- nom ;
- URL ;
- identifiant externe ;
- statut ;
- date de première découverte ;
- date de dernière synchronisation.

### Document

Un document représente une unité documentaire stable.

Exemples :

- une vidéo YouTube ;
- un billet de blog ;
- un PDF ;
- une intervention parlementaire ;
- un discours.

Champs principaux :

- identifiant technique ;
- identifiant permanent ;
- source d'origine ;
- clé d'origine ;
- type de document ;
- titre ;
- auteur ;
- URL originale ;
- date de découverte.

### Version de document

Une version représente un état observé d'un document.

Elle permet de conserver l'historique lorsqu'un contenu change.

Champs principaux :

- identifiant technique ;
- document associé ;
- numéro de version ;
- date de capture ;
- empreinte du contenu ;
- titre observé ;
- contenu ou référence vers le contenu archivé.

### Transcription

Une transcription est liée à une version de document.

Champs principaux :

- identifiant technique ;
- version du document ;
- langue ;
- texte ;
- horodatages ;
- méthode de transcription ;
- date de création.

### Analyse

Une analyse est un enrichissement produit à partir d'une version ou d'une transcription.

Elle est indépendante du document.

Champs principaux :

- identifiant technique ;
- document ou version associée ;
- type d'analyse ;
- modèle utilisé ;
- version du prompt ;
- résultat ;
- date de génération.

### Publication

Une publication représente la forme visible par le lecteur.

Champs principaux :

- identifiant technique ;
- document associé ;
- URL publique ;
- statut ;
- date de publication ;
- date de dernière mise à jour.

## Relations

Une source possède plusieurs documents.

Un document possède plusieurs versions.

Une version peut posséder une transcription.

Une transcription peut posséder plusieurs analyses.

Un document peut posséder une publication.

## Principes

### 1. Le registre documentaire est la source de vérité

Aucun module ne contourne le registre.

### 2. Un document est identifié avant d'être enrichi

L'identifiant permanent naît au moment de l'enregistrement du document.

### 3. Les documents sont stables

Un document n'est pas remplacé lorsqu'un contenu change.

### 4. Les versions conservent l'historique

Une modification de contenu crée une nouvelle version.

### 5. Les analyses sont régénérables

Une analyse peut être supprimée puis recalculée sans modifier le document.

### 6. Le domaine ne dépend pas de la technique

Les modèles métier ne dépendent pas de PostgreSQL, Qdrant, YouTube ou OpenAI.

## Schéma conceptuel

```text
Source
  └── Document
        └── DocumentVersion
              ├── Transcript
              └── Analysis

Document
  └── Publication
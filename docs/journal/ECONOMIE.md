# Économie d'InsouWiki

Les sources sont redécouvertes régulièrement ; les documents ne sont indexés qu’une fois, sauf décision explicite de réindexation.

## Philosophie

InsouWiki distingue deux types de coûts :

- les coûts de constitution du patrimoine documentaire ;
- les coûts de consultation du patrimoine documentaire.

L'objectif est que la consultation du site ne dépende pas des services d'intelligence artificielle.

Les appels à des modèles externes doivent être réalisés principalement lors de l'indexation des sources.

Une fois indexé, un document appartient au patrimoine documentaire d'InsouWiki et peut être consulté autant de fois que nécessaire sans nouvelle consommation d'API.

---

## Cycle documentaire

Source
↓
Découverte
↓
Téléchargement
↓
Transcription
↓
Segmentation
↓
Embeddings (future V2)
↓
Base documentaire
↓
Recherche
↓
Consultation

---

## Coûts d'indexation

Une seule fois par document.

Exemples :

- transcription audio ;
- génération des embeddings ;
- enrichissements éventuels.

Ces coûts constituent un investissement.

---

## Coûts de consultation

Aucun appel OpenAI.

Les recherches utilisent uniquement :

- PostgreSQL ;
- Qdrant (recherche sémantique) ;
- les données déjà indexées.

Le coût dépend uniquement de l'infrastructure d'hébergement.

---

## Coûts optionnels

Certaines fonctionnalités pourront utiliser un modèle de langage :

- synthèse documentaire ;
- comparaison entre auteurs ;
- génération de dossiers documentaires.

Ces fonctionnalités devront rester facultatives.

La consultation des sources restera toujours possible sans IA générative.

---

## Principe

Les contenus générés par l'IA doivent pouvoir être régénérés à tout moment.

La valeur d'InsouWiki réside dans son patrimoine documentaire, pas dans les réponses ponctuelles d'un modèle de langage.

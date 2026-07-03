# Journal de développement

## Sprint 13.0 — Intégration de `SimpleDivergenceFinder`

### Objectif

Poursuivre l’enrichissement progressif de l’expérience documentaire en raccordant `SimpleDivergenceFinder` au service d’exploration, sans modifier l’architecture existante.

### Réalisation

`SimpleExplorationService` orchestre désormais quatre raisonneurs documentaires :

* `SimpleContinuityFinder`
* `SimpleEvolutionFinder`
* `SimpleConvergenceFinder`
* `SimpleDivergenceFinder`

`SimpleExplorationBuilder` reste inchangé. Il reçoit une liste d’observations documentaires et assemble une `DocumentaryExploration`, sans connaître les raisonneurs qui les ont produites.

### Validation

Un nouveau test vérifie qu’une divergence documentaire détectée apparaît dans les observations de l’exploration.

Le premier passage des tests a montré qu’une même exploration pouvait produire à la fois une observation d’évolution et une observation de divergence. Le test a donc été ajusté pour refléter le comportement réel du moteur d’exploration.

**Résultat : 44 tests passent.**

### Bilan architectural

Ce sprint confirme le patron d’intégration des raisonneurs documentaires.

L’ajout d’un quatrième raisonneur n’a nécessité aucune modification du Builder ni du modèle d’exploration. Seul le service d’orchestration a évolué, conformément à sa responsabilité.

L’architecture accueille désormais plusieurs observations simultanées, ce qui rapproche l’exploration documentaire de l’expérience de lecture visée par InsouWiki.

### Prochaine étape

Prendre un point d’étape sur le moteur d’exploration afin d’observer ce qu’il produit désormais avec quatre raisonneurs connectés, avant d’ajouter de nouvelles capacités.

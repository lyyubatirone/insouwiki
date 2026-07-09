# Architecture des services

Ce document décrit les différentes familles de services utilisées dans InsouWiki.

Son objectif est de faciliter la compréhension du domaine et de guider les futures évolutions de l'architecture.

---

## Builders

Construisent un objet documentaire à partir d'informations existantes.

Exemples :

- SimpleKnowledgeBuilder
- SimpleDocumentaryPieceBuilder
- SimpleDocumentaryDossierBuilder
- SimpleExplorationBuilder

---

## Finders

Recherchent ou détectent des éléments documentaires.

Exemples :

- SimpleContinuityFinder
- SimpleConvergenceFinder
- SimpleDivergenceFinder
- SimpleEvolutionFinder
- SimpleDocumentaryRelationFinder

---

## Analyzers

Produisent une analyse documentaire explicable.

Exemples :

- DocumentaryReasoningAnalyzer

---

## Services d'orchestration

Coordonnent plusieurs services documentaires.

Exemples :

- SimpleExplorationService
- SimpleDocumentarySequencer

---

## Services d'infrastructure

Interagissent avec des systèmes externes.

Exemples :

- DiscoveryService
- AudioExtractionService
- OpenAITranscriptionProvider
- YouTubeAudioExtractor
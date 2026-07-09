# Architecture des services

## Objectif

Décrire les différentes responsabilités des services utilisés dans InsouWiki.

Ce document évoluera au fur et à mesure des découvertes du domaine.

---

## Builder

### Responsabilité

Construire un objet documentaire à partir d'informations existantes.

### Produit

Un objet du domaine.

---

## Finder

### Responsabilité

Rechercher ou détecter des éléments documentaires.

### Produit

Des informations documentaires permettant d'alimenter d'autres traitements.

---

## Analyzer

### Responsabilité

Produire une analyse documentaire explicable à partir d'observations et d'indicateurs.

### Produit

Une `DocumentaryAnalysis`.

---

## Service d'orchestration

### Responsabilité

Coordonner plusieurs services documentaires afin de réaliser une opération métier.

### Produit

Dépend du cas d'usage.

Un Builder construit un objet du domaine à partir d'informations existantes. Il n'effectue ni recherche documentaire, ni analyse documentaire, ni prise de décision.
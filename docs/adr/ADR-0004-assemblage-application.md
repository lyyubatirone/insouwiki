# ADR-0004 — Assemblage de l'application

## Statut

Acceptée

---

## Contexte

Au fur et à mesure du développement d'InsouWiki, la ligne de commande (`CLI`) est amenée à utiliser un nombre croissant de services :

* DiscoveryService
* AudioExtractionService
* TranscriptionService
* futurs services documentaires.

Sans organisation particulière, la CLI deviendrait progressivement responsable de construire les repositories, les extracteurs, les providers et leurs dépendances techniques.

Cette responsabilité ne lui appartient pas.

---

## Décision

InsouWiki introduit un point d'assemblage unique de l'application.

Cet objet est responsable de construire les services et de leur fournir leurs dépendances.

La CLI ne crée jamais directement une dépendance technique.

Elle demande simplement à l'application le service dont elle a besoin.

Les services continuent de dépendre d'interfaces plutôt que d'implémentations concrètes.

---

## Conséquences

Cette décision apporte plusieurs bénéfices :

* la CLI reste simple ;
* les dépendances techniques sont centralisées ;
* les services restent indépendants des technologies utilisées ;
* le remplacement d'une implémentation (PostgreSQL, OpenAI, yt-dlp, etc.) n'impacte pas la CLI ;
* les tests deviennent plus simples grâce à l'injection de dépendances.

---

## Principes retenus

L'assemblage de l'application constitue une responsabilité à part entière.

Les responsabilités du projet deviennent :

* le domaine décrit les concepts documentaires ;
* les services orchestrent les traitements ;
* les interfaces définissent les contrats ;
* les implémentations dialoguent avec les technologies externes ;
* l'application assemble ces composants ;
* la CLI dialogue uniquement avec l'utilisateur.

---

## Alternatives étudiées

### Instancier directement les dépendances dans la CLI

Cette solution est simple au début du projet.

Elle devient rapidement difficile à maintenir lorsque le nombre de services augmente.

Elle est donc écartée.

### Utiliser un framework d'injection de dépendances

Cette solution est volontairement écartée.

Les besoins actuels d'InsouWiki ne justifient pas l'introduction d'un framework supplémentaire.

Une implémentation simple et explicite est privilégiée.

---

## Motivation

Cette décision prolonge un principe déjà appliqué dans tout le projet :

> Le domaine documentaire gouverne l'architecture technique.

Les dépendances techniques doivent rester au service du modèle documentaire et non l'inverse.

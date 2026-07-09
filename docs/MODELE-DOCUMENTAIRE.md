# Modèle documentaire


## Objet

Le modèle documentaire d'InsouWiki décrit les objets documentaires,
leurs propriétés et les relations qui les unissent.

Il constitue le langage commun utilisé par l'ensemble du projet.

Le modèle documentaire ne cherche pas à interpréter le réel.

Il cherche à représenter fidèlement les éléments documentés afin de
permettre au lecteur de les explorer, de les vérifier et de construire
sa propre compréhension.

---
## Entité documentaire

Une entité documentaire représente un objet du monde réel identifié
de manière univoque dans le patrimoine documentaire d'InsouWiki.

Une entité documentaire possède une identité permanente qui ne dépend
ni de ses relations, ni de ses fonctions, ni des événements de son
existence.

Elle constitue un point d'ancrage stable permettant de relier les
documents, les connaissances et les relations documentaires.

Les informations susceptibles d'évoluer au cours du temps (fonctions,
appartenances, mandats, responsabilités...) ne font pas partie de
l'identité de l'entité. Elles sont représentées par des relations
documentaires datées et documentées.

# Principe fondateur

Les objets documentaires ne sont pas créés parce qu'ils sont utiles
à l'informatique.

Ils sont créés parce qu'ils représentent une réalité documentaire
observable.

La technique s'adapte au modèle documentaire.

Le modèle documentaire ne s'adapte pas à la technique.

---

# Les grandes familles documentaires

Le patrimoine documentaire d'InsouWiki est organisé autour de plusieurs
familles d'objets.

## Sources

Les sources constituent l'origine du patrimoine documentaire.

Elles permettent au lecteur de revenir à l'information originale.

---

## Documents

Les documents représentent les contenus documentaires collectés.

Ils constituent la matière première du patrimoine documentaire.

---

## Connaissances

Les connaissances sont construites exclusivement à partir des documents.

Elles restent toujours reliées aux sources qui permettent leur
vérification.

---

## Entités documentaires

Les entités documentaires représentent les acteurs, organisations,
institutions, lieux ou événements évoqués dans les documents.

---

## Contextes documentaires

Les contextes documentaires décrivent les circonstances dans lesquelles
une information est produite.

Ils permettent de comprendre une déclaration sans en modifier le contenu.

---

## Relations documentaires

Les relations documentaires décrivent les liens objectifs entre les
objets du patrimoine documentaire.

Chaque relation possède une signification documentaire explicite.

Aucune relation importante ne doit être déduite lorsqu'elle peut être
documentée.

---

# Philosophie

Le modèle documentaire est conçu pour permettre au lecteur d'explorer
librement le patrimoine documentaire.

Il n'a pas pour objectif de conduire le lecteur vers une conclusion.

Il lui fournit les moyens d'exercer son propre jugement à partir des
sources documentaires.

---

## Les relations documentaires

Les relations documentaires décrivent les liens existant entre les
entités du patrimoine documentaire.

Une relation est un objet documentaire à part entière.

Elle possède sa propre identité documentaire et peut évoluer au cours
du temps indépendamment des entités qu'elle relie.

### Éléments constitutifs (version de travail)

Les éléments suivants sont actuellement identifiés comme nécessaires :

- entité source ;
- type de relation ;
- entité cible ;
- date de début éventuelle ;
- date de fin éventuelle ;
- justification documentaire.

Cette liste reste volontairement ouverte.

Le modèle documentaire évoluera au fur et à mesure de la découverte
de nouveaux besoins documentaires.

## Pistes de réflexion

Les travaux de modélisation laissent entrevoir une organisation du
graphe documentaire autour de faits documentaires.

Un fait documentaire pourrait relier des entités au moyen d'une relation
documentée, située dans le temps et justifiée par une ou plusieurs
sources primaires.

Cette hypothèse n'est pas encore intégrée au modèle documentaire.
Elle sera confrontée aux futurs cas documentaires avant toute décision
d'architecture.

## La pièce documentaire

La pièce documentaire est la plus petite unité documentaire capable
d'établir une information.

Elle constitue l'unité de preuve du patrimoine documentaire d'InsouWiki.

Une pièce documentaire est toujours issue d'un document, lui-même
rattaché à une source primaire.

Une ou plusieurs pièces documentaires peuvent justifier :

- une connaissance ;
- une relation documentaire ;
- d'autres objets documentaires définis par le modèle.

La pièce documentaire permet au lecteur de revenir précisément au passage
du document qui établit l'information.

Une observation documentaire décrit ce que le document montre.

Un indice documentaire exprime ce que le métier permet d'en déduire.

Une décision documentaire résulte de la combinaison de plusieurs indices documentaires.
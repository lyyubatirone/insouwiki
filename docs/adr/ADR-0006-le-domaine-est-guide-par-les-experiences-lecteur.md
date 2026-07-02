# ADR-0006 — Le domaine est guidé par les expériences lecteur

## Statut

Accepté

---

# Contexte

Au cours des premiers sprints d'InsouWiki, les concepts documentaires ont été introduits progressivement.

Aucun n'a été créé à partir d'une architecture technique prédéfinie.

Chaque nouveau concept est apparu lorsqu'une nouvelle expérience documentaire devait être rendue possible pour le lecteur.

Ainsi sont notamment apparus :

* les faits documentaires ;
* les relations documentaires ;
* les connaissances documentaires ;
* les évolutions documentaires ;
* les sujets documentaires.

Cette manière de concevoir le domaine s'est révélée plus simple, plus cohérente et plus stable que l'ajout anticipé de concepts.

---

# Décision

Le domaine documentaire d'InsouWiki est désormais guidé par les expériences que le lecteur doit pouvoir vivre.

Le processus de conception suit l'ordre suivant :

Expérience lecteur

↓

Raisonnement documentaire

↓

Concepts du domaine

↓

Tests

↓

Code

Les besoins techniques ne créent jamais, à eux seuls, un nouveau concept documentaire.

---

# Conséquences

Avant d'introduire un nouvel objet métier, une question devra toujours être posée :

> Quelle expérience documentaire rend-il possible ?

Si cette question ne possède pas de réponse claire, le concept ne doit pas être ajouté.

Inversement, lorsqu'une expérience documentaire ne peut être représentée correctement par le domaine existant, celui-ci doit évoluer.

Le domaine accompagne ainsi naturellement les besoins documentaires du lecteur.

---

# Principes

Le lecteur constitue le point de départ de la réflexion documentaire.

Les raisonnements documentaires organisent les preuves.

Les concepts du domaine permettent de représenter ces raisonnements.

Les tests protègent durablement les règles documentaires.

Le code constitue l'implémentation de ces règles.

---

# Motivation

Cette approche présente plusieurs avantages.

Elle limite l'introduction de concepts inutiles.

Elle réduit les anticipations techniques.

Elle favorise une architecture stable.

Elle garantit que chaque élément du domaine possède une utilité documentaire clairement identifiée.

---

# Vision

InsouWiki n'est pas conçu autour de fonctionnalités.

Il est conçu autour des parcours intellectuels que le lecteur doit pouvoir accomplir.

Le domaine documentaire évolue donc au rythme des expériences documentaires rendues possibles.

Cette progression permet de construire un patrimoine documentaire cohérent, durable et fidèle aux principes fondateurs du projet.

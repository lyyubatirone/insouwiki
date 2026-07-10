# État du chantier

Dernière mise à jour : Sprint 17

## Sprint en cours

**Sprint 17**

### Question directrice

Qu'est-ce qu'une observation documentaire ?

---

## Dernières découvertes stabilisées

- DocumentaryIndicator
- DocumentaryAnalysis
- Les méthodes documentaires
- Les analyseurs documentaires produisent une analyse, jamais une décision.
- Distinction entre patrimoine documentaire, méthodologique et logiciel.
- La fidélité constitue le principe directeur du projet.

---

## Hypothèses en cours

- Définition de l'observation documentaire.
- Distinction entre observation et qualification.
- Nature des opérations intellectuelles du documentaliste.

---

## Documents récemment créés

- METHODES-DOCUMENTAIRES.md
- INDICATEURS-DOCUMENTAIRES.md

---

## ADR

- ADR-0007 : à rédiger.

---

## État des tests

73 tests verts.

---

## Prochaine étape

ENQUETE-0001 — Observation documentaire.

## Observation du Sprint 17.8

Les services de type `Finder` ne produisent pas encore de `DocumentaryAnalysis`.

Ils retournent aujourd'hui des observations textuelles.

Hypothèse à vérifier :
un `Finder` repère des éléments documentaires, tandis qu'un `Analyzer` produit une analyse documentaire explicable.

conserver non seulement ce que nous faisons, mais aussi pourquoi nous le faisons... et parfois pourquoi nous choisissons de ne pas le faire.

Question ouverte : le tri des pièces documentaires appartient-il au Builder ou à une stratégie d'ordonnancement documentaire ?

Hypothèse V1 : une séquence documentaire produit un fait documentaire. Cette hypothèse devra être réévaluée lorsque plusieurs faits pourront être extraits d'une même séquence.

## Clarification V1

La priorité de la V1 est de permettre à l'utilisateur de retrouver des passages pertinents à partir d'une question ou d'une affirmation.

InsouWiki fonctionne d'abord comme un moteur documentaire appliqué à des sources audiovisuelles transcrites.

Les faits documentaires, relations, connaissances et dossiers enrichissent progressivement cette recherche, mais ne sont pas nécessaires pour produire une première valeur utilisateur.

Le 10 juillet 2026, InsouWiki a effectué sa première recherche documentaire complète sur une source réelle.
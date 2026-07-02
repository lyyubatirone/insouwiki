# Corpus documentaire de référence

## Objectif

Le corpus documentaire de référence constitue un patrimoine documentaire miniature utilisé pour observer l'évolution d'InsouWiki.

Il ne s'agit pas d'un jeu de tests techniques, mais d'un scénario documentaire stable permettant d'évaluer l'expérience proposée au lecteur.

Chaque nouvelle capacité documentaire devra pouvoir être observée sur ce corpus avant d'être considérée comme intégrée au projet.

---

# Principes

Le corpus de référence doit rester :

* petit ;
* compréhensible par un lecteur humain ;
* stable dans le temps ;
* riche en situations documentaires.

Chaque fait documentaire est volontairement choisi afin d'illustrer un comportement attendu du moteur d'exploration.

---

# Premier scénario documentaire

## Sujet

Retraites

## Question du lecteur

Le lecteur souhaite comprendre les positions exprimées par plusieurs auteurs sur le départ à la retraite.

Il cherche notamment à savoir :

- quelles positions sont partagées ;
- quelles positions divergent ;
- si une même position est restée stable dans le temps ;
- quelles observations documentaires permettent de mieux comprendre ce sujet.

### Corpus

| Auteur             | Date | Affirmation                     |
| ------------------ | ---- | ------------------------------- |
| Jean-Luc Mélenchon | 2017 | La retraite doit être à 60 ans. |
| Jean-Luc Mélenchon | 2022 | La retraite doit être à 60 ans. |
| François Ruffin    | 2023 | La retraite doit être à 60 ans. |
| Jordan Bardella    | 2024 | La retraite doit être à 65 ans. |

---

# Exploration documentaire attendue

Le lecteur devrait pouvoir constater que :

* une continuité documentaire existe concernant la position de Jean-Luc Mélenchon ;
* une convergence documentaire existe entre Jean-Luc Mélenchon et François Ruffin ;
* une divergence documentaire existe entre Jean-Luc Mélenchon et Jordan Bardella ;
* une évolution documentaire est détectée par le moteur d'exploration selon son implémentation actuelle.

---

# Rôle du corpus

Ce corpus n'a pas vocation à vérifier des algorithmes.

Les tests unitaires remplissent déjà cette fonction.

Le corpus de référence sert à observer le comportement global d'InsouWiki lorsqu'un lecteur explore un sujet documentaire.

Il permet de répondre à une question simple :

> « L'expérience documentaire produite est-elle pertinente pour le lecteur ? »

---

# Évolution

Ce document est destiné à évoluer avec InsouWiki.

À mesure que de nouveaux raisonneurs documentaires apparaîtront, le corpus sera enrichi afin de représenter les nouvelles situations documentaires rencontrées.

Le corpus de référence devient ainsi un patrimoine documentaire au service du développement lui-même.

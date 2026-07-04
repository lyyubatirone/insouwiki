# Cas documentaires

## Objet

Ce document recense les situations documentaires rencontrées lors de la
conception d'InsouWiki.

Il ne décrit pas les solutions techniques.

Il décrit les situations que le modèle documentaire doit être capable de
représenter fidèlement.

Chaque nouveau cas rencontré permet d'enrichir progressivement le modèle
documentaire.

---

# Cas documentaire CD-001

## Situation

Une personnalité change de groupe parlementaire sans changer de
formation politique.

## Pourquoi est-ce important ?

Le lecteur doit pouvoir replacer chaque déclaration dans son contexte
institutionnel au moment où elle a été prononcée.

## Objets concernés

- Personne
- Groupe parlementaire
- Formation politique

## Relations concernées

- est membre de

## Informations indispensables

- date de début de la relation ;
- date de fin éventuelle ;
- justification documentaire.

## Questions ouvertes

Aucune.

---

# Cas documentaire CD-002

## Situation

Une personnalité cesse d'exercer un mandat.

Exemple :
Jean-Luc Mélenchon n'est plus député.

## Pourquoi est-ce important ?

Une déclaration ancienne doit être présentée avec le mandat exercé au
moment où elle a été prononcée.

## Objets concernés

- Personne
- Mandat

## Relations concernées

- exerce le mandat

## Informations indispensables

- période de validité ;
- justification documentaire.

## Questions ouvertes

Le mandat doit-il être représenté comme une entité documentaire ou comme
un type particulier de relation ?

---

# Cas documentaire CD-003

## Situation

Une commission parlementaire appartient à une institution.

Exemple :
La Commission des finances appartient à l'Assemblée nationale.

## Pourquoi est-ce important ?

Le lecteur doit comprendre l'organisation institutionnelle dans laquelle
une déclaration est produite.

## Objets concernés

- Commission parlementaire
- Institution

## Relations concernées

- fait partie de

## Informations indispensables

- justification documentaire.

## Questions ouvertes

Cette relation est-elle considérée comme permanente ou simplement
stable dans le temps ?

---

# Évolution du document

Ce document est volontairement évolutif.

Chaque nouveau cas documentaire découvert est ajouté avant toute
évolution du modèle ou du code.

Le réel guide le modèle documentaire.

Le modèle documentaire guide le code.
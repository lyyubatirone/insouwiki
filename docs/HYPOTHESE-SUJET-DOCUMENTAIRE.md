# HYPOTHÈSE — LE SUJET DOCUMENTAIRE

## Statut

**Hypothèse en cours d'étude**

Ce document ne décrit pas un concept établi du domaine.

Il formalise une intuition apparue au cours du Sprint 8 afin de la confronter progressivement aux besoins documentaires d'InsouWiki.

Aucune décision d'architecture ne découle de ce document tant que cette hypothèse n'a pas été validée.

---

# Question

Existe-t-il, entre les faits documentaires et les connaissances documentaires, un concept appelé **Sujet documentaire** ?

Autrement dit :

Les connaissances sont-elles construites directement à partir des faits, ou sont-elles d'abord organisées autour d'un sujet documentaire ?

---

# Intuition

Lorsqu'un utilisateur interroge InsouWiki, il ne recherche généralement pas une connaissance déjà construite.

Il recherche un sujet.

Exemples :

* l'autonomie de la Corse ;
* la retraite à 60 ans ;
* le nucléaire ;
* l'Union européenne.

Ces sujets semblent constituer des points d'entrée naturels dans le patrimoine documentaire.

---

# Hypothèse

Un sujet documentaire pourrait représenter l'ensemble documentaire relatif à un même thème.

Il rassemblerait notamment :

* les faits documentaires ;
* les relations documentaires ;
* les documents concernés ;
* les auteurs impliqués ;
* les périodes couvertes.

Les connaissances documentaires seraient ensuite construites à partir de ce patrimoine organisé.

---

# Premières observations

Cette hypothèse semble compatible avec plusieurs cas d'usage.

## Exemple 1

Question :

> « Que dit Jean-Luc Mélenchon sur l'autonomie de la Corse ? »

Le système semble naturellement identifier le sujet documentaire :

> Autonomie de la Corse.

Il rassemble ensuite les faits et les relations avant de produire une réponse.

---

## Exemple 2

Question :

> « Comment la position de Jean-Luc Mélenchon sur l'Union européenne a-t-elle évolué ? »

Le sujet documentaire demeure :

> Union européenne.

La connaissance recherchée concerne l'évolution de cette position.

---

## Exemple 3

Question :

> « Quels arguments sont avancés pour défendre la retraite à 60 ans ? »

Le sujet documentaire reste identifiable avant même la construction des connaissances.

---

# Éléments à vérifier

Cette hypothèse devra être confrontée aux questions suivantes :

* Existe-t-il des recherches qui ne correspondent à aucun sujet documentaire identifiable ?
* Un même fait documentaire peut-il appartenir à plusieurs sujets documentaires ?
* Les sujets documentaires sont-ils découverts automatiquement ou définis explicitement ?
* Le sujet documentaire constitue-t-il un véritable objet du domaine ou simplement un mécanisme de classement ?

---

# Critères de validation

L'hypothèse pourra être retenue si elle :

* simplifie le modèle documentaire ;
* améliore la compréhension du domaine ;
* facilite la construction des connaissances ;
* respecte les principes de traçabilité et de neutralité documentaire.

Dans le cas contraire, elle sera abandonnée sans remettre en cause le reste du domaine.

---

# Principe méthodologique

Cette hypothèse illustre la méthode de conception d'InsouWiki.

Une intuition n'entre pas immédiatement dans le domaine.

Elle suit les étapes suivantes :

Intuition

↓

Discussion

↓

Confrontation au domaine

↓

Validation ou abandon

↓

Documentation du domaine

↓

Implémentation

Le domaine documentaire ne s'enrichit que des concepts qui résistent à cette démarche.

---

# Conclusion provisoire

À ce stade du projet, le **Sujet documentaire** apparaît comme une piste prometteuse.

Aucune décision n'est encore prise.

Le domaine documentaire déterminera lui-même, au fil des prochains sprints, si ce concept mérite d'intégrer durablement l'architecture d'InsouWiki.

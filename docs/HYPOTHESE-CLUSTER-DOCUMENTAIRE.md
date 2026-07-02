# HYPOTHÈSE — CLUSTER DOCUMENTAIRE

## Objet

Ce document explore une possible évolution du domaine documentaire d'InsouWiki.

Il ne décrit pas un concept validé.

Il formalise une intuition apparue lors de la construction du premier `SimpleKnowledgeBuilder`.

---

# Contexte

Le `SimpleKnowledgeBuilder` reçoit actuellement :

* une liste de faits documentaires ;
* une liste de relations documentaires.

Il réalise deux opérations distinctes :

1. identifier les groupes de faits reliés ;
2. construire les connaissances documentaires correspondantes.

Cette double responsabilité conduit à s'interroger sur une éventuelle séparation de ces traitements.

---

# Hypothèse

Il pourrait exister un concept intermédiaire :

le **Cluster documentaire**.

Un cluster documentaire représenterait un ensemble cohérent de faits documentaires reliés entre eux.

Il ne constituerait pas encore une connaissance documentaire.

Il représenterait uniquement une organisation du patrimoine documentaire.

---

# Responsabilité possible

Le cluster documentaire aurait pour seule responsabilité :

regrouper des faits documentaires appartenant au même ensemble documentaire.

Il ne produirait :

* aucune synthèse ;
* aucune interprétation ;
* aucune connaissance.

Il décrirait uniquement une structure.

---

# Construction

Le cluster documentaire pourrait être construit exclusivement à partir :

* des faits documentaires ;
* des relations documentaires.

La méthode de regroupement pourrait évoluer dans le temps sans modifier les objets représentant les connaissances documentaires.

---

# Conséquence architecturale

Cette hypothèse conduirait à distinguer deux responsabilités :

```text
Faits documentaires
        │
Relations documentaires
        │
        ▼
Clusters documentaires
        │
        ▼
KnowledgeBuilder
        │
        ▼
Connaissances documentaires
```

Le `KnowledgeBuilder` ne découvrirait plus les groupes de faits.

Il transformerait simplement des clusters documentaires en connaissances documentaires.

---

# Intérêt

Cette séparation présenterait plusieurs avantages :

* responsabilité plus claire de chaque service ;
* évolution indépendante des stratégies de regroupement ;
* simplification du `KnowledgeBuilder` ;
* meilleure réutilisation des regroupements documentaires.

---

# Questions ouvertes

Cette hypothèse soulève plusieurs questions.

Le cluster documentaire constitue-t-il réellement un concept du domaine ?

Ou bien s'agit-il uniquement d'un détail d'implémentation destiné à faciliter la construction des connaissances ?

Cette distinction devra être confrontée aux futurs besoins du projet.

En particulier :

* la détection des sujets documentaires ;
* les regroupements chronologiques ;
* les regroupements par événements ;
* les raisonnements documentaires plus complexes.

---

# État actuel

À ce stade du projet, cette hypothèse n'est pas validée.

Le `SimpleKnowledgeBuilder` continue d'assurer lui-même le regroupement des faits documentaires.

Cette solution demeure satisfaisante tant que les traitements restent simples.

L'hypothèse sera réévaluée lorsque plusieurs stratégies de regroupement documentaire apparaîtront naturellement.

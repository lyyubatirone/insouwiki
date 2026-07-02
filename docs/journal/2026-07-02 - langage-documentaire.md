# Journal de développement — Sprint 8

## La chaîne documentaire est désormais complète

Aujourd'hui marque une étape majeure dans la construction d'InsouWiki.

Le projet est désormais capable de représenter l'ensemble de sa chaîne documentaire, depuis la source primaire jusqu'à la connaissance documentaire.

Cette progression s'est construite progressivement, sans remettre en cause les concepts établis précédemment.

Chaque nouveau niveau enrichit le patrimoine documentaire tout en conservant la traçabilité complète des niveaux qui le précèdent.

La chaîne documentaire devient ainsi :

```
Source primaire
        │
        ▼
Document
        │
        ▼
Transcription
        │
        ▼
TranscriptionSegment
        │
        ▼
DocumentarySequence
        │
        ▼
DocumentaryFact
        │
        ▼
DocumentaryRelation
        │
        ▼
Knowledge
```

Cette architecture constitue désormais le modèle documentaire de référence d'InsouWiki.

---

## Les relations documentaires

Le Sprint 8 a permis d'introduire les relations documentaires.

Une relation documentaire décrit un lien explicite entre plusieurs faits documentaires.

Elle ne remplace jamais les faits.

Elle organise le patrimoine documentaire sans modifier les observations qu'il contient.

Cette découverte a conduit à la création :

* de `DocumentaryRelationType` ;
* de `DocumentaryRelation` ;
* de `DocumentaryRelationFinder` ;
* de `SimpleDocumentaryRelationFinder`.

---

## Les connaissances documentaires

Le Sprint 8 a également permis de définir le concept de connaissance documentaire.

Une connaissance est désormais définie comme une organisation explicable de faits documentaires reliés entre eux par des relations documentaires.

Une connaissance ne constitue jamais une interprétation indépendante.

Elle demeure entièrement reconstructible à partir des faits documentaires qui la composent.

Cette propriété constitue un principe fondamental d'InsouWiki.

---

## Les hypothèses documentaires

Le Sprint 8 introduit également une nouvelle catégorie de documents :

les hypothèses documentaires.

Contrairement aux documents de domaine, elles ne décrivent pas un concept établi.

Elles permettent d'explorer des intuitions avant leur éventuelle intégration au domaine documentaire.

La première hypothèse concerne le **Sujet documentaire**.

Cette idée n'est pas encore considérée comme un objet du domaine.

Elle sera confrontée aux futurs besoins documentaires avant toute décision.

Cette démarche formalise une nouvelle étape de notre méthode de conception :

```
Intuition
    ↓
Discussion
    ↓
Confrontation au domaine
    ↓
Validation ou abandon
    ↓
Documentation
    ↓
Implémentation
```

---

## Le premier constructeur de connaissances

Le Sprint 8 voit également apparaître le premier `SimpleKnowledgeBuilder`.

Son implémentation demeure volontairement minimale.

Elle valide l'architecture documentaire sans anticiper les futures stratégies de construction des connaissances.

Comme pour les précédents services, cette première implémentation constitue une base de travail destinée à évoluer progressivement.

---

## Qualité

Le projet compte désormais :

* 24 tests automatisés ;
* un modèle documentaire complet ;
* une architecture documentaire stable depuis la source primaire jusqu'à la connaissance documentaire.

Les invariants documentaires demeurent intégralement respectés.

---

## Regard sur cette étape

Ce Sprint marque probablement la fin de la construction des objets fondamentaux du domaine.

Les prochains développements porteront principalement sur l'amélioration des traitements documentaires plutôt que sur la création de nouveaux concepts.

InsouWiki possède désormais les éléments nécessaires pour transformer progressivement un document en une connaissance documentaire vérifiable.

La suite du projet consistera à rendre cette chaîne toujours plus pertinente, plus précise et plus fidèle aux sources primaires.

Cette étape constitue l'un des jalons majeurs de la naissance d'InsouWiki.

# Les deux moteurs d'InsouWiki

Au cours de la conception du projet, il est apparu qu'InsouWiki répond à deux besoins distincts du lecteur.

Le premier consiste à vérifier rapidement ce qui a réellement été dit à partir des sources primaires.

Le second consiste à explorer un patrimoine documentaire afin de mettre en évidence différentes relations documentaires.

Ces deux besoins reposent sur les mêmes documents, mais poursuivent des objectifs différents.

---

## Moteur de vérification documentaire

Le moteur de vérification constitue le point d'entrée naturel d'InsouWiki.

Sa mission est de construire un dossier documentaire composé de pièces documentaires permettant au lecteur de vérifier immédiatement une affirmation.

Son fonctionnement peut être représenté ainsi :

```text
Document
    ↓
Transcription
    ↓
Séquence documentaire
    ↓
Pièce documentaire
    ↓
Dossier documentaire
```

Ce moteur ne produit aucune interprétation.

Il rassemble et présente fidèlement les éléments permettant au lecteur de consulter les sources primaires.

La première réponse d'InsouWiki appartient à ce moteur.

---

## Moteur d'exploration documentaire

Le moteur d'exploration intervient après la constitution du dossier documentaire.

Il aide le lecteur à parcourir ce dossier en mettant en évidence différents phénomènes documentaires.

Son fonctionnement peut être représenté ainsi :

```text
Document
    ↓
Transcription
    ↓
Séquence documentaire
    ↓
Fait documentaire
    ↓
Raisonneurs documentaires
    ↓
Exploration documentaire
```

Les raisonneurs détectent notamment :

* les continuités documentaires ;
* les convergences documentaires ;
* les divergences documentaires ;
* les évolutions documentaires.

Ils n'interprètent jamais les documents.

Ils proposent des modes de lecture supplémentaires du patrimoine documentaire.

---

## Complémentarité

Les deux moteurs partagent le même patrimoine documentaire.

Ils répondent cependant à deux questions différentes.

Le moteur de vérification répond à la question :

> « Que s'est-il réellement dit ? »

Le moteur d'exploration répond à la question :

> « Quelles relations documentaires peut-on observer entre ces éléments ? »

La vérification documentaire constitue la finalité première d'InsouWiki.

L'exploration documentaire enrichit cette vérification sans jamais s'y substituer.

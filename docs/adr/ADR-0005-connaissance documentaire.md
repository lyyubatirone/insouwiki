# ADR-0005 — La connaissance documentaire est produite par transformations successives

## Statut

Acceptée

## Contexte

Le premier document vivant a démontré qu'InsouWiki est capable de produire une transcription complète à partir d'une source audiovisuelle.

Le projet entre désormais dans une nouvelle phase.

L'objectif n'est plus seulement de collecter des documents mais de construire progressivement une connaissance documentaire vérifiable.

Cette évolution nécessite de définir la manière dont une source est transformée en connaissance.

## Décision

InsouWiki ne produit jamais directement une connaissance finale.

Chaque traitement transforme un résultat documentaire en un nouveau résultat documentaire.

La chaîne documentaire suit le principe suivant :

```
Source
    ↓
Document
    ↓
Audio
    ↓
Transcription
    ↓
Segments documentaires
    ↓
Faits documentaires
    ↓
Connaissances reliées
```

Chaque étape possède :

* une responsabilité unique ;
* des entrées clairement définies ;
* des sorties documentaires explicites ;
* une traçabilité complète vers l'étape précédente.

Aucune étape ne doit supprimer les résultats des étapes antérieures.

Chaque transformation enrichit le patrimoine documentaire sans jamais remplacer les informations existantes.

## Conséquences

Cette architecture présente plusieurs avantages.

Les traitements deviennent indépendants les uns des autres.

Chaque étape peut être améliorée ou remplacée sans remettre en cause le reste du système.

Les résultats intermédiaires restent disponibles pour être vérifiés, corrigés ou retraités.

La traçabilité documentaire est conservée tout au long de la chaîne de transformation.

Enfin, cette approche permet d'introduire progressivement de nouvelles capacités documentaires sans modifier les traitements existants.

## Principe fondamental

InsouWiki ne produit pas directement de la connaissance.

Il transforme progressivement les documents jusqu'à rendre cette connaissance observable, vérifiable et traçable.

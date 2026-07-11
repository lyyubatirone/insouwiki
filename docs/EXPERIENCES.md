# Expériences documentaires

Ce document consigne les expériences réalisées pendant le développement
d'InsouWiki.

Chaque expérience vise à répondre à une question documentaire.
Les décisions sont prises à partir des résultats observés, et non d'hypothèses.

---

# EXP-0001 — Comparaison des moteurs de transcription

## Question

Quelle stratégie de transcription permet de servir le mieux la mission documentaire d'InsouWiki ?

## Pourquoi cette expérience ?

Le lecteur doit pouvoir :

- retrouver précisément un passage ;
- disposer d'une transcription fidèle ;
- ouvrir immédiatement la vidéo au bon moment.

Nous devons déterminer si un seul moteur répond à ces trois exigences ou si une stratégie combinée est préférable.

## Corpus

Vidéo :

« Ma réaction au vote pour l'autonomie de la Corse »

## Moteurs évalués

- gpt-4o-mini-transcribe
- whisper-1 (verbose_json)

## Critères d'évaluation

- fidélité de la transcription ;
- ponctuation ;
- noms propres ;
- découpage naturel ;
- précision des horodatages ;
- facilité d'intégration.

## Résultats

GPT produit une excellente transcription textuelle mais ne fournit pas de segmentation exploitable.

Whisper fournit une transcription correcte accompagnée de 118 segments horodatés.

Ces segments permettent de construire directement les séquences documentaires.

La recherche sur le terme « autonomie » retourne six passages distincts correctement horodatés.

## Enseignement

Au début de cette réflexion, l'idée était d'ajouter de nouvelles méthodes au DocumentRepository.

L'observation du domaine a conduit à renoncer à cette solution.

Il est apparu que le besoin ne concerne pas le stockage des documents mais leur observation globale.

Cette décision confirme une nouvelle fois le principe fondateur du projet :

Le domaine guide toujours le code.

## Conclusion

La segmentation fournie par Whisper constitue une excellente unité documentaire.

Le domaine a été enrichi avec l'objet TranscriptionSegment.

Les DocumentarySequence sont désormais construites à partir de ces segments.

Le DocumentaryReasoningAnalyzer conserve son rôle de regroupement documentaire, mais n'est plus responsable de la segmentation.

## Décision

Conserver Whisper comme base d'indexation documentaire pour la V1.

Poursuivre l'évaluation de GPT-4o Mini Transcribe pour la qualité linguistique.


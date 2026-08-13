# ADR-0009 — Architecture de transcription documentaire

## Statut

Acceptée

## Contexte

InsouWiki doit transformer des sources audiovisuelles en transcriptions
exploitables comme documents vérifiables et traçables.

Une transcription utile à InsouWiki doit permettre :

- de restituer fidèlement les propos ;
- de rattacher le texte au moment où il est prononcé dans la source ;
- de distinguer les locuteurs lorsque cette distinction a une valeur
  documentaire ;
- de traiter des documents audiovisuels longs ;
- de conserver un coût compatible avec le traitement d'un corpus
  important.

Les expériences EXP-0002 à EXP-0005 ont étudié plusieurs modèles et
plusieurs conditions de transcription.

Elles ont notamment montré que :

- `gpt-4o-mini-transcribe` produit un texte de bonne qualité mais ne
  fournit pas les timestamps nécessaires à notre usage ;
- `whisper-1` fournit une segmentation temporelle exploitable ;
- les longues sources doivent être découpées pour éviter la troncature ;
- un recouvrement entre chunks permet de préserver les phrases
  traversant une frontière ;
- le texte de `gpt-4o-mini-transcribe` peut être aligné localement sur
  les timestamps de `whisper-1` avec une forte similarité ;
- cet alignement reste robuste dans des conditions acoustiques ou
  d'élocution moins favorables ;
- la diarisation est utile lorsque plusieurs locuteurs ont une
  importance documentaire, mais inutilement coûteuse et complexe
  lorsqu'un seul locuteur est significatif.

Les similarités observées lors des expériences d'alignement sont :

| Condition | Similarité |
|---|---:|
| Son propre et diction claire | 0.989 |
| Bruit de manifestation | 0.969 |
| Diction difficile | 0.966 |

Le détail expérimental est conservé dans :

`docs/experiments/EXP-0002-0005-TRANSCRIPTION.md`

## Décision

InsouWiki adopte deux stratégies de transcription selon la nature
documentaire de la source.

### 1. Documents mono-locuteur

Pour les documents dans lesquels un seul locuteur est
documentairement significatif, la chaîne de transcription sera :

```text
source audiovisuelle
        ↓
extraction audio
        ↓
découpage avec recouvrement
        ↓
gpt-4o-mini-transcribe
        ↓
texte
        +
whisper-1
        ↓
timestamps
        ↓
alignement local
        ↓
fusion des frontières
        ↓
segments documentaires horodatés
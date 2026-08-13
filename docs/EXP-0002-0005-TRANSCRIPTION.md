# EXP-0002 à EXP-0005 — Architecture de transcription

## Objet

Ces expériences ont pour objectif de déterminer une architecture de
transcription adaptée aux exigences documentaires d'InsouWiki.

La transcription produite par InsouWiki doit permettre :

- de restituer fidèlement les propos tenus ;
- de rattacher les propos à leur position temporelle dans la source ;
- de distinguer les locuteurs lorsque cela est nécessaire ;
- de permettre la consultation du passage original ;
- de rester économiquement compatible avec le traitement d'un corpus
  documentaire important.

La qualité recherchée n'est donc pas seulement linguistique.

Elle est documentaire.

---

# EXP-0002 — Comparaison initiale des modèles

## Source

Vidéo comportant plusieurs intervenants.

Durée de l'audio :

- environ 687 secondes ;
- plusieurs échanges entre intervenants ;
- quatre interlocuteurs humains considérés comme significatifs à
  l'écoute.

## whisper-1

Résultat :

- langue détectée : français ;
- durée : 687,38 s ;
- 290 segments ;
- timestamps directement disponibles.

L'écoute de plusieurs passages répartis dans le document montre une
transcription globalement fidèle.

Quelques expressions sont incorrectement reconnues, mais les erreurs
observées ne compromettent généralement pas la compréhension du propos.

### Usage

```text
{'seconds': 688.0, 'type': 'duration'}
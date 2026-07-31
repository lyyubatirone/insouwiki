# Enquêtes documentaires

Ce document conserve les principales découvertes réalisées au cours de la conception d'InsouWiki.

Contrairement aux ADR, qui décrivent des décisions d'architecture, les enquêtes documentaires retracent les enseignements tirés de l'observation du domaine.

Une enquête peut conduire à :

* une nouvelle compréhension du domaine ;
* la confirmation d'un modèle existant ;
* l'abandon d'une hypothèse ;
* l'identification d'un futur besoin.

Une enquête n'a pas pour objectif de produire du code. Elle a pour objectif de mieux comprendre la réalité documentaire avant toute évolution du logiciel.

---

# Enquête documentaire n°1

## Question

Quelle est la finalité réelle d'InsouWiki ?

Au cours de cette enquête, plusieurs hypothèses ont été examinées concernant les faits documentaires, les raisonneurs et le parcours de l'utilisateur.

L'analyse a progressivement déplacé la réflexion de l'architecture logicielle vers l'usage réel du logiciel.

## Constat

L'utilisateur ne consulte pas InsouWiki pour obtenir une interprétation.

Il souhaite avant tout vérifier rapidement ce qui a réellement été dit sur un sujet à partir des sources primaires.

L'exploration documentaire constitue un moyen de faciliter cette vérification, mais ne représente pas la finalité du projet.

## Découvertes

### La finalité d'InsouWiki

La fonction première d'InsouWiki est la vérification documentaire.

L'exploration documentaire est un moyen de faciliter cette vérification, jamais une fin en soi.

### La première réponse

La première réponse fournie au lecteur doit être suffisamment fidèle et contextualisée pour être utile immédiatement.

Elle ne doit jamais obliger le lecteur à vérifier.

Elle doit toujours lui permettre de vérifier.

### Le contexte documentaire

Une citation ne doit jamais être isolée de son contexte.

Le lecteur doit pouvoir accéder facilement à la séquence documentaire, à la transcription complète et au document d'origine.

La possibilité de remonter jusqu'à la source constitue une propriété essentielle d'InsouWiki.

### Le rôle des raisonneurs

Les raisonneurs documentaires détectent des phénomènes documentaires.

Ils ne produisent aucune interprétation.

Ils guident le lecteur vers les séquences pertinentes, sans jamais conclure à sa place.

## Conséquences pour le projet

Cette enquête confirme plusieurs principes fondateurs :

* aucune interprétation n'est produite par InsouWiki ;
* les citations demeurent prioritaires sur toute reformulation ;
* le contexte documentaire est toujours préservé ;
* chaque information reste traçable jusqu'à sa source ;
* les évolutions futures devront être évaluées à l'aune d'une question simple :

> Est-ce que cette évolution aide réellement le lecteur à vérifier ce qui a été dit ?

---

# Enquête documentaire n°2

## Question

À quoi ressemble la première réponse idéale d'InsouWiki ?

Cette enquête est née d'une réflexion sur le comportement réel des lecteurs.

L'objectif n'était plus de concevoir une interface ou un algorithme, mais de comprendre ce qu'une personne attend lorsqu'elle souhaite vérifier une affirmation relayée dans le débat public.

## Constat

Le lecteur ne cherche pas d'abord une synthèse.

Il souhaite accéder le plus rapidement possible à ce qui a réellement été dit.

La première réponse d'InsouWiki doit donc présenter une preuve documentaire avant toute forme d'analyse ou de synthèse.

## Découvertes

### Le dossier de preuves

InsouWiki ne produit pas une réponse au sens classique du terme.

Il construit un dossier de preuves à partir des sources primaires.

Ce dossier rassemble les éléments permettant au lecteur de vérifier lui-même les affirmations qui l'intéressent.

### La première réponse

La première réponse doit être une citation suffisamment longue pour rester fidèle au propos exprimé.

Elle est accompagnée de son contexte documentaire :

* l'auteur ;
* le document d'origine ;
* la date ;
* la séquence documentaire.

Le lecteur peut ensuite accéder directement à la séquence, à la transcription complète et au document original.

### L'exploration

Après cette première preuve, le lecteur peut poursuivre son exploration.

InsouWiki lui propose d'autres séquences documentaires relatives au même sujet.

Le logiciel n'impose pas un parcours unique.

Il propose plusieurs modes d'exploration du même dossier documentaire.

### Les modes de consultation

Le contenu du dossier documentaire demeure identique.

Seule sa présentation peut évoluer selon les besoins du lecteur.

Celui-ci pourra notamment choisir différents modes de consultation, comme l'ordre chronologique, la pertinence documentaire ou d'autres organisations du dossier.

## Conséquences pour le projet

Cette enquête confirme que la finalité d'InsouWiki n'est pas de produire une interprétation ou une synthèse.

Sa mission consiste à construire un dossier de preuves fidèle aux sources primaires.

L'exploration documentaire devient un ensemble d'outils permettant au lecteur de parcourir ce dossier selon ses propres besoins, sans que le logiciel ne privilégie une lecture particulière.

Toute évolution future devra préserver cette liberté d'exploration tout en maintenant une traçabilité complète jusqu'aux sources originales.

ENQUÊTE DOCUMENTAIRE

Retrouver une déclaration dont on ne se souvient
qu'approximativement.
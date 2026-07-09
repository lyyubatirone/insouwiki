# Méthodes documentaires

## Pourquoi ce document ?

Une méthode documentaire décrit la manière dont un documentaliste exploite des observations documentaires afin de produire une analyse explicable.

Une méthode documentaire ne prend jamais directement une décision.

Elle expose :

- les observations réalisées ;
- les indicateurs documentaires mobilisés ;
- le raisonnement suivi ;
- l'analyse produite.

La décision éventuelle appartient toujours au composant qui consomme cette analyse.

Cette séparation garantit que le raisonnement documentaire demeure :

- explicable ;
- traçable ;
- reproductible.

---

# Structure d'une méthode documentaire

Chaque méthode documentaire est décrite selon la structure suivante.

## Objectif

Quelle question documentaire la méthode cherche-t-elle à résoudre ?

---

## Observations documentaires

Quelles observations peuvent être réalisées sur les documents ?

---

## Indicateurs documentaires

Quels indicateurs permettent de qualifier ces observations ?

---

## Analyse produite

Quelle DocumentaryAnalysis la méthode produit-elle ?

---

## Limites

Dans quels cas cette méthode ne permet-elle pas de conclure ?

---

## Analyseurs

Quels composants logiciels implémentent cette méthode documentaire ?

---

# Catalogue des méthodes

Les méthodes documentaires sont progressivement découvertes au cours du développement.

Aucune méthode n'est créée sans avoir été observée, documentée et validée.

Les premières méthodes identifiées sont :

- Continuité dialogique (en cours de formalisation)

D'autres méthodes apparaîtront progressivement :

- Convergence documentaire
- Divergence documentaire
- Changement de sujet
- Reformulation
- Digression
- Référence documentaire

Cette liste n'est pas figée.

Elle évolue avec la découverte du domaine.

---

# Principe fondamental

Une méthode documentaire appartient au patrimoine méthodologique.

Elle est indépendante de son implémentation logicielle.

Le logiciel n'est que la traduction fidèle d'une méthode documentaire préalablement définie.

# Méthode documentaire n°1

# Continuité dialogique

## Objectif

Déterminer si deux séquences documentaires appartiennent au même raisonnement.

La méthode ne cherche pas à établir si les affirmations sont vraies ou fausses.

Elle cherche uniquement à déterminer si le second passage constitue la poursuite du raisonnement engagé dans le premier.

---

## Question documentaire

Les deux séquences appartiennent-elles au même raisonnement ?

---

## Observations documentaires

Le documentaliste observe notamment :

- l'identité du locuteur ;
- la proximité temporelle des séquences ;
- la continuité du vocabulaire ;
- la présence de connecteurs logiques ;
- la reprise d'un sujet déjà introduit ;
- l'absence de rupture explicite du discours.

---

## Indicateurs documentaires

Les observations peuvent conduire à identifier plusieurs indicateurs.

Par exemple :

- Continuité dialogique ;
- Transition explicite.

Ces indicateurs ne prennent pas la décision.

Ils qualifient les observations réalisées.

---

## Analyse produite

La méthode produit une DocumentaryAnalysis contenant :

- les observations réalisées ;
- les indicateurs identifiés ;
- une explication du raisonnement suivi ;
- une conclusion proposée.

Cette analyse est entièrement explicable.

---

## Décision

La méthode ne décide jamais si les deux séquences doivent être regroupées.

Cette décision appartient au composant qui utilise l'analyse.

---

## Limites

La méthode ne permet pas toujours de conclure.

Certaines situations nécessitent une interprétation humaine, notamment :

- les ruptures implicites de sujet ;
- les changements progressifs de raisonnement ;
- les discours très elliptiques.

Dans ces cas, l'analyse documentaire doit refléter les incertitudes observées.

---

## Implémentation actuelle

Cette méthode est actuellement implémentée par :

DocumentaryReasoningAnalyzer


# Définition d'un analyseur documentaire

## Définition

Un analyseur documentaire est un composant dont la responsabilité est d'appliquer une méthode documentaire à une ou plusieurs observations afin de produire une analyse documentaire explicable.

Il ne prend jamais directement une décision métier.

---

## Responsabilités

Un analyseur documentaire :

* observe les éléments documentaires qui lui sont confiés ;
* identifie les indicateurs documentaires pertinents ;
* applique une méthode documentaire ;
* produit une `DocumentaryAnalysis`.

Il ne modifie jamais les documents analysés.

Il ne décide jamais de l'action à entreprendre.

---

## Entrées

Un analyseur reçoit un ou plusieurs objets du domaine documentaire.

Par exemple :

* une séquence documentaire ;
* deux séquences successives ;
* un fait documentaire ;
* un ensemble de faits documentaires.

---

## Sortie

Un analyseur produit toujours une `DocumentaryAnalysis`.

Cette analyse contient notamment :

* les observations réalisées ;
* les indicateurs mobilisés ;
* l'explication du raisonnement suivi ;
* une conclusion proposée.

---

## Principe d'explicabilité

Chaque élément de l'analyse doit pouvoir être justifié par les observations effectivement réalisées.

Une analyse documentaire n'affirme jamais davantage que ce que les observations permettent d'établir.

---

## Principe de traçabilité

Le raisonnement suivi par l'analyseur doit pouvoir être reconstitué.

Chaque conclusion proposée doit pouvoir être reliée :

* aux observations ;
* aux indicateurs ;
* à la méthode documentaire appliquée.

---

## Principe d'indépendance

Une méthode documentaire existe indépendamment de son implémentation logicielle.

Un analyseur documentaire constitue une implémentation de cette méthode.

Plusieurs analyseurs peuvent implémenter la même méthode, à condition de produire des analyses conformes à sa spécification.

---

## Conséquence

La qualité d'un analyseur documentaire ne se mesure pas uniquement à la pertinence de sa conclusion.

Elle se mesure également à sa capacité à expliquer fidèlement le raisonnement documentaire ayant conduit à cette conclusion.

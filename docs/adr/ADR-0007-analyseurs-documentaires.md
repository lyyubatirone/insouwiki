# ADR-0007

## Titre

Les analyseurs documentaires produisent une analyse, pas une décision.

---

## Statut

Accepté

---

## Contexte

Les premiers analyseurs documentaires retournaient directement une décision métier, généralement sous la forme d'un booléen.

Cette approche mélangeait deux responsabilités :

- analyser les observations documentaires ;
- prendre une décision à partir de cette analyse.

Au cours du Sprint 17, le domaine a été clarifié.

Une analyse documentaire constitue un objet métier autonome.

Elle doit pouvoir être expliquée, vérifiée et réutilisée indépendamment de la décision finale.

---

## Décision

Tout analyseur documentaire doit produire une `DocumentaryAnalysis`.

Cette analyse contient notamment :

- les observations réalisées ;
- les indicateurs identifiés ;
- l'explication du raisonnement ;
- une conclusion proposée.

La décision finale appartient au composant qui consomme cette analyse.

---

## Conséquences

### Positives

- séparation claire des responsabilités ;
- meilleure explicabilité ;
- meilleure traçabilité ;
- meilleure testabilité ;
- réutilisation des analyses par plusieurs composants.

### Contraintes

Les analyseurs deviennent légèrement plus riches, puisqu'ils produisent un objet métier plutôt qu'un simple booléen.

Cette complexité supplémentaire est acceptée car elle reflète fidèlement le domaine documentaire.

---

## Justification documentaire

Une analyse documentaire n'est pas une décision.

Elle constitue l'explication du raisonnement documentaire ayant conduit à une conclusion proposée.

Cette distinction améliore la fidélité du logiciel au travail du documentaliste.
# Journal de développement — Sprint 9

## Le patrimoine documentaire devient un réseau de connaissances

Aujourd'hui, InsouWiki franchit une nouvelle étape dans son évolution.

Après avoir construit progressivement l'ensemble de son patrimoine documentaire, le projet devient capable d'organiser automatiquement les faits documentaires en connaissances.

Cette évolution ne repose plus sur une simple propriété des faits, comme leur auteur.

Elle s'appuie désormais sur les relations documentaires qui relient les faits entre eux.

Le raisonnement documentaire commence ainsi à exploiter la structure même du patrimoine documentaire.

---

## Les relations deviennent actives

Jusqu'à présent, les relations documentaires constituaient un élément du patrimoine.

Elles étaient décrites, stockées et vérifiées.

À partir de ce Sprint, elles deviennent également un outil de construction des connaissances.

Le `SimpleKnowledgeBuilder` n'utilise plus directement les attributs des faits pour les regrouper.

Il exploite les relations documentaires existantes afin d'identifier des ensembles cohérents de faits.

Cette évolution renforce considérablement la séparation des responsabilités :

* le `DocumentaryRelationFinder` découvre les relations ;
* le `KnowledgeBuilder` exploite ces relations pour organiser les connaissances.

Chaque service conserve ainsi une responsabilité documentaire clairement définie.

---

## Le graphe documentaire apparaît naturellement

Cette évolution fait émerger une nouvelle propriété du patrimoine documentaire.

Les faits documentaires et leurs relations forment naturellement un réseau.

Chaque groupe de faits reliés constitue une composante cohérente de ce réseau.

Le `SimpleKnowledgeBuilder` identifie automatiquement ces groupes et construit une connaissance documentaire pour chacun d'eux.

Cette approche ne nécessite pas l'introduction d'un nouvel objet métier.

Le graphe documentaire apparaît naturellement comme une conséquence du modèle documentaire construit depuis les premiers sprints.

Cette découverte confirme la pertinence de la méthode de conception adoptée par le projet : laisser le domaine révéler progressivement ses propres structures.

---

## Une évolution de la philosophie du projet

Cette étape marque également une évolution importante dans la manière de concevoir InsouWiki.

Les premiers sprints avaient pour objectif de représenter fidèlement le patrimoine documentaire.

Le Sprint 9 inaugure une nouvelle phase :

organiser ce patrimoine afin de permettre de nouveaux raisonnements documentaires.

Le projet entre progressivement dans une logique d'exploration documentaire plutôt que de simple accumulation de documents.

---

## Le domaine continue de guider l'architecture

L'algorithme utilisé pour regrouper les faits n'a pas été choisi pour sa sophistication.

Il a été retenu parce qu'il constitue la traduction la plus fidèle du domaine documentaire.

Cette étape illustre une nouvelle fois le principe fondateur du projet :

> Le domaine gouverne le projet.

Les choix techniques demeurent au service des concepts documentaires et non l'inverse.

---

## Qualité

Le projet compte désormais :

* 25 tests automatisés ;
* un `SimpleKnowledgeBuilder` capable de construire plusieurs connaissances documentaires à partir des relations existantes ;
* un premier raisonnement documentaire fondé sur la structure du patrimoine documentaire.

Le patrimoine documentaire n'est plus seulement conservé.

Il devient progressivement explorable et organisable.

---

## Regard sur cette étape

Ce Sprint marque probablement le début d'une nouvelle période dans l'histoire d'InsouWiki.

Les objets fondamentaux du domaine sont désormais en place.

Les prochains développements porteront principalement sur la richesse des raisonnements documentaires qu'il sera possible de construire à partir d'eux.

Le projet ne cherche plus seulement à conserver des preuves.

Il apprend désormais à les organiser afin de rendre le patrimoine documentaire plus intelligible, tout en conservant la possibilité permanente de revenir aux sources primaires.

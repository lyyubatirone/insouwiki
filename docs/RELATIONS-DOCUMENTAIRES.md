# Évolution de la compréhension des relations documentaires

Les premiers développements d'InsouWiki ont conduit à considérer les relations documentaires comme un ensemble homogène.

Les travaux du Sprint 9 montrent qu'elles remplissent en réalité des responsabilités différentes.

Cette distinction permet de mieux comprendre leur rôle dans la construction des connaissances documentaires.

---

# Les relations de structuration

Les relations de structuration ont pour objectif d'organiser le patrimoine documentaire.

Elles permettent d'identifier des ensembles cohérents de faits documentaires.

Ces relations servent notamment à construire les connaissances documentaires.

Exemples possibles :

* même sujet documentaire ;
* même événement ;
* même document ;
* même contexte documentaire.

Ces relations répondent à la question :

> **Quels faits appartiennent naturellement au même ensemble documentaire ?**

---

# Les relations d'analyse

Les relations d'analyse décrivent une propriété observable entre plusieurs faits documentaires.

Elles n'ont pas pour objectif de constituer un même ensemble documentaire.

Elles enrichissent la compréhension du patrimoine documentaire.

Exemples possibles :

* contradiction ;
* évolution ;
* précision ;
* complément ;
* conséquence.

Ces relations répondent à la question :

> **Que peut-on observer entre ces faits documentaires ?**

---

# Conséquences sur l'architecture

Cette distinction clarifie les responsabilités des services documentaires.

Le `KnowledgeBuilder` exploite uniquement les relations de structuration afin de constituer des connaissances documentaires.

Les relations d'analyse sont utilisées par des services spécialisés, chargés d'explorer le patrimoine documentaire et de mettre en évidence certaines propriétés, comme les contradictions ou les évolutions.

Cette séparation permet à chaque service de conserver une responsabilité documentaire clairement identifiée.

---

# Évolution du domaine

Cette distinction n'introduit pas un nouveau concept documentaire.

Elle précise le rôle des relations déjà présentes dans le domaine.

Elle permettra au patrimoine documentaire de s'enrichir progressivement sans remettre en cause les objets fondamentaux construits lors des précédents sprints.

# Les relations documentaires

## Pourquoi ce document ?

Le patrimoine documentaire d'InsouWiki n'est pas constitué uniquement de documents.

Il est constitué d'entités documentaires reliées entre elles par des relations documentaires.

Ces relations donnent leur sens aux documents et permettent de répondre aux enquêtes documentaires du lecteur.

---

# Les entités documentaires

Une entité documentaire représente un élément identifiable du patrimoine documentaire.

Par exemple :

- une personnalité
- un document
- une pièce documentaire
- une connaissance documentaire
- une organisation
- une institution
- une chaîne documentaire
- un corpus documentaire

Ces entités possèdent une identité permanente.

---

# Les relations documentaires

Les entités documentaires sont reliées par des relations.

Par exemple :

Une personnalité peut :

- être propriétaire d'un corpus documentaire ;
- être l'auteur d'un document ;
- intervenir dans un document ;
- être locuteur d'une pièce documentaire ;
- être citée dans une pièce documentaire.

Une organisation peut :

- publier un document ;
- organiser un événement ;
- être mentionnée dans une pièce documentaire.

Ces relations constituent le véritable graphe documentaire d'InsouWiki.

---

# Les enquêtes documentaires

Le lecteur ne choisit jamais un type de relation.

Il formule une question documentaire.

Il précise éventuellement son enquête grâce à des critères documentaires.

Le moteur documentaire recherche ensuite toutes les relations pertinentes permettant de répondre à cette enquête.

---

# L'interface

L'interface présente une vision unifiée du patrimoine documentaire.

Le lecteur voit :

- une personnalité ;
- une enquête ;
- des pièces documentaires.

Le domaine, lui, distingue les différentes relations qui justifient la présence de chaque pièce documentaire.

Ainsi :

Une même personnalité peut être reliée à une pièce documentaire par plusieurs relations simultanément.

Cette complexité appartient au domaine.

Elle ne doit jamais compliquer l'expérience du lecteur.

---

# Traçabilité

Chaque pièce documentaire doit pouvoir expliquer pourquoi elle apparaît dans une enquête documentaire.

Cette justification fait partie intégrante du patrimoine documentaire.

Elle doit rester consultable à tout moment.

---

# Principe fondamental

Le domaine distingue.

L'interface unifie.

Le lecteur mène une enquête documentaire.

InsouWiki utilise les relations documentaires pour lui présenter toutes les pièces pertinentes, sans jamais perdre la traçabilité de leur origine.

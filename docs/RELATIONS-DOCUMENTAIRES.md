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

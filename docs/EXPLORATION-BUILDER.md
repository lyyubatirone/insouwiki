# EXPLORATION BUILDER

## Objet

L'Exploration Builder est le service chargé de construire une exploration documentaire.

Il constitue le point de rencontre entre le patrimoine documentaire et l'expérience du lecteur.

---

# Pourquoi ce service existe

Les différents services documentaires d'InsouWiki produisent des éléments spécialisés :

* des faits documentaires ;
* des connaissances documentaires ;
* des observations documentaires ;
* des évolutions ;
* des convergences ;
* des divergences.

Aucun de ces services n'a pour responsabilité d'organiser ces éléments dans une expérience d'exploration.

Cette responsabilité appartient à l'Exploration Builder.

---

# Responsabilité

L'Exploration Builder :

* reçoit une intention d'exploration ;
* reçoit une ou plusieurs portes d'entrée documentaires ;
* sélectionne les éléments documentaires pertinents ;
* construit une exploration documentaire cohérente.

Il ne crée jamais de nouveaux faits.

Il ne produit aucune interprétation.

Il assemble les résultats existants.

---

# Ce que l'Exploration Builder ne fait pas

L'Exploration Builder :

* ne transcrit pas les documents ;
* n'extrait pas les faits ;
* ne construit pas les connaissances ;
* ne détecte pas les évolutions ;
* ne détecte pas les convergences ;
* ne détecte pas les divergences.

Ces responsabilités appartiennent à d'autres services.

---

# Les entrées

Le service reçoit notamment :

* une intention d'exploration ;
* une porte d'entrée documentaire.

À terme, il pourra également recevoir :

* des préférences d'exploration ;
* un niveau d'approfondissement souhaité ;
* d'autres paramètres liés à l'expérience du lecteur.

---

# Les sorties

Le résultat du service est une `DocumentaryExploration`.

Cette exploration contient progressivement :

* des Exploration Items ;
* les liens vers les preuves correspondantes.

---

# Le rôle de l'intelligence artificielle

L'intelligence artificielle peut aider à sélectionner les éléments les plus pertinents.

Elle ne modifie jamais le patrimoine documentaire.

Elle contribue uniquement à organiser le parcours proposé au lecteur.

---

# Vision

L'Exploration Builder constitue le chef d'orchestre de l'expérience documentaire.

Les autres services produisent les briques documentaires.

L'Exploration Builder les assemble afin que le lecteur puisse parcourir le patrimoine documentaire de manière progressive, transparente et vérifiable.

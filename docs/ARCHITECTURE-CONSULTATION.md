# Architecture de consultation

## Objectif

Cette couche a pour rôle de rendre le patrimoine documentaire
consultable par les interfaces d'InsouWiki.

Elle constitue le point d'entrée privilégié des applications
(web, API, outils d'administration…) vers les données
documentaires.

Elle ne réalise aucune analyse documentaire.

Elle ne construit aucune connaissance.

Elle expose uniquement des informations déjà présentes dans le
patrimoine documentaire.

---

# Position dans l'architecture

```
                   Interface Web
                         │
                         ▼
              DocumentaryLibrary
                         │
        ┌────────────────┴────────────────┐
        ▼                                 ▼
Repositories                     Services documentaires
        │                                 │
        └────────────────┬────────────────┘
                         ▼
              Patrimoine documentaire
```

La couche de consultation isole les interfaces des détails
d'implémentation.

Une page web ne connaît jamais directement :

- PostgreSQL ;
- Qdrant ;
- les repositories ;
- les services internes.

Elle dialogue uniquement avec la bibliothèque documentaire.

---

# Responsabilités

La couche de consultation peut notamment :

- retrouver une personnalité ;
- retrouver un document ;
- retrouver une pièce documentaire ;
- retrouver une connaissance ;
- retrouver une relation documentaire ;
- compter les documents associés à une personnalité ;
- fournir des listes destinées à l'affichage.

---

# Ce qu'elle ne fait jamais

La couche de consultation ne doit jamais :

- analyser un document ;
- produire une connaissance ;
- modifier le patrimoine documentaire ;
- lancer une collecte ;
- effectuer une transcription ;
- indexer des contenus.

Ces responsabilités appartiennent aux autres couches
d'InsouWiki.

---

# Principe fondamental

Les interfaces ne consultent jamais directement le patrimoine
documentaire.

Elles interrogent toujours la bibliothèque documentaire.

Cette séparation garantit :

- une architecture stable ;
- des interfaces indépendantes du stockage ;
- une évolution possible des mécanismes internes sans impact
  sur les applications clientes.

---

# Vision

À terme, toutes les interfaces d'InsouWiki utiliseront cette
couche :

- interface Web ;
- API publique ;
- outils d'administration ;
- applications tierces.

La bibliothèque documentaire constitue la porte d'entrée
unique vers le patrimoine documentaire.
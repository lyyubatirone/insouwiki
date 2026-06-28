# Architecture de l'application

## Objectif

Ce document décrit la manière dont les composants d'InsouWiki sont assemblés.

Il ne décrit pas le métier documentaire lui-même, mais l'organisation générale de l'application.

L'objectif est de garantir que la ligne de commande, les services, les repositories et les intégrations externes restent clairement séparés.

---

# Principe général

InsouWiki repose sur une séparation simple :

```text
CLI
 │
 ▼
Application
 │
 ▼
Services
 │
 ▼
Interfaces
 │
 ▼
Implémentations
```

La CLI ne construit pas directement les dépendances techniques.

Elle demande à l'application les services dont elle a besoin.

---

# Rôle de la CLI

La ligne de commande a trois responsabilités :

* recevoir les paramètres de l'utilisateur ;
* appeler le service approprié ;
* afficher le résultat.

Elle ne doit pas contenir de logique métier.

Elle ne doit pas connaître les détails techniques des implémentations.

---

# Rôle de l'application

L'application est le point d'assemblage du système.

Elle construit les services et leur fournit leurs dépendances.

Par exemple :

```text
Application
 ├── DiscoveryService
 ├── AudioExtractionService
 ├── TranscriptionService
 ├── DocumentRepository
 ├── AudioExtractor
 └── TranscriptionProvider
```

L'application ne contient pas de logique documentaire.

Elle assemble les composants.

---

# Rôle des services

Les services orchestrent les opérations documentaires.

Exemples :

* découvrir des documents ;
* extraire l'audio ;
* produire une transcription.

Un service ne dépend pas directement d'une technologie externe.

Il dépend d'une interface.

---

# Rôle des interfaces

Les interfaces définissent des contrats.

Exemples :

```text
DocumentRepository
AudioExtractor
TranscriptionProvider
```

Elles permettent de remplacer une implémentation sans modifier le domaine ni les services.

---

# Rôle des implémentations

Les implémentations parlent au monde extérieur.

Exemples :

* PostgreSQL ;
* YouTube ;
* yt-dlp ;
* OpenAI.

Elles doivent rester isolées du domaine métier.

---

# Schéma global

```text
Utilisateur
    │
    ▼
CLI
    │
    ▼
Application
    │
    ├───────────────┬────────────────────┬────────────────────┐
    ▼               ▼                    ▼                    ▼
DiscoveryService   AudioExtractionService TranscriptionService Repositories
    │               │                    │                    │
    ▼               ▼                    ▼                    ▼
YouTubeCollector   AudioExtractor        TranscriptionProvider PostgreSQL
                    │                    │
                    ▼                    ▼
              YouTubeAudioExtractor   OpenAI / Dummy
```

---

# Principe de dépendance

Les dépendances vont toujours du plus général vers le plus concret.

Le domaine ne dépend de rien.

Les services dépendent du domaine et des interfaces.

Les implémentations dépendent des bibliothèques externes.

La CLI dépend de l'application.

---

# Règle d'architecture

Toute dépendance externe doit passer par une interface.

Ainsi, InsouWiki peut remplacer une technologie sans modifier son modèle documentaire.

---

# Conclusion

L'objet Application constitue le point d'assemblage d'InsouWiki.

Il permet à la CLI de rester simple, aux services de rester indépendants, et aux implémentations techniques de rester remplaçables.

Cette organisation garantit que le code reste fidèle au modèle documentaire du projet.

## Évolution de l'architecture

Cette architecture pourra évoluer dans le futur afin de mieux distinguer le domaine, l'application et les intégrations techniques.

Cette évolution ne sera entreprise que lorsqu'un besoin concret apparaîtra.

InsouWiki privilégie la stabilité de son architecture plutôt que des réorganisations anticipées. Une évolution structurelle n'est justifiée que lorsqu'elle simplifie réellement le développement, améliore la lisibilité du projet ou répond à un nouveau besoin documentaire.

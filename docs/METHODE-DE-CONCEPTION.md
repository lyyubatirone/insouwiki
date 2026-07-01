# MÉTHODE DE CONCEPTION

## Objet

Ce document décrit la méthode utilisée pour concevoir InsouWiki.

Il ne constitue pas une méthode générale de développement logiciel.

Il présente la discipline de conception adoptée pour construire un patrimoine documentaire durable, vérifiable et évolutif.

---

# Principe

Dans InsouWiki, le code ne constitue jamais le point de départ.

Toute évolution commence par une compréhension du domaine documentaire.

Le logiciel est la conséquence de cette compréhension.

---

# Les étapes de conception

Chaque évolution importante suit les étapes suivantes.

## 1. Comprendre

Une nouvelle idée est discutée.

L'objectif est de comprendre le besoin documentaire avant toute décision technique.

Aucune solution n'est retenue tant que le problème n'est pas clairement identifié.

---

## 2. Nommer

Lorsqu'un nouveau concept apparaît, il reçoit un nom précis.

Le vocabulaire constitue une partie du modèle documentaire.

Un concept mal nommé est généralement un concept mal compris.

---

## 3. Documenter

Le concept est décrit dans un document métier.

Les principes, les responsabilités et les relations avec les autres concepts y sont définis.

Cette documentation précède toujours le développement.

---

## 4. Décider

Lorsque la décision possède un impact durable sur l'architecture ou la méthode documentaire, elle est consignée dans une ADR.

Les ADR expliquent les choix.

Elles ne remplacent ni le domaine ni la documentation.

---

## 5. Modéliser

Le concept devient un objet du domaine.

Cet objet représente une réalité documentaire.

Il reste indépendant des technologies utilisées pour le produire.

---

## 6. Vérifier

Des tests sont écrits afin d'exprimer les invariants du domaine.

Les tests protègent les règles documentaires.

Ils ne vérifient pas uniquement le fonctionnement du code.

---

## 7. Implémenter

Les services, les fournisseurs et les composants techniques sont développés.

Ils appliquent les règles définies par le domaine.

La technologie demeure au service de la méthode documentaire.

---

# Les principes de conception

## Le domaine avant la technique

Les choix techniques ne doivent jamais imposer le modèle documentaire.

Les technologies peuvent évoluer.

Le domaine doit rester stable.

---

## La preuve avant la confiance

Toute fonctionnalité doit préserver ou renforcer la possibilité de retrouver les preuves documentaires.

Une amélioration technique qui éloigne le lecteur de la preuve est contraire à la philosophie d'InsouWiki.

---

## La simplicité avant l'anticipation

Chaque objet contient uniquement les informations nécessaires à sa responsabilité.

Les besoins futurs ne justifient pas l'ajout prématuré de nouveaux concepts ou attributs.

Le modèle évolue progressivement.

---

## Les invariants avant les algorithmes

Les règles du domaine sont définies avant les traitements qui les utilisent.

Les algorithmes peuvent évoluer.

Les invariants constituent les fondations du modèle.

---

## L'immuabilité des observations

Les objets représentant des observations documentaires sont considérés comme immuables.

Ils décrivent un état du patrimoine documentaire à un instant donné.

Une correction produit une nouvelle observation plutôt qu'une modification silencieuse de l'ancienne.

---

## Une transformation à la fois

Chaque étape de la chaîne documentaire enrichit uniquement le résultat de l'étape précédente.

Aucune transformation ne saute une étape.

Cette progression garantit la traçabilité complète de la connaissance.

---

# Le rôle de l'intelligence artificielle

L'intelligence artificielle n'est jamais considérée comme une autorité documentaire.

Elle constitue un outil d'assistance.

Les règles documentaires sont définies par InsouWiki.

Les modèles d'intelligence artificielle sont évalués selon leur capacité à respecter ces règles.

---

# Le rôle des tests

Les tests ne servent pas uniquement à détecter des régressions.

Ils constituent une expression exécutable des règles du domaine.

Ils participent à la documentation vivante du projet.

---

# Évolution

Cette méthode de conception pourra évoluer à mesure que le domaine documentaire sera mieux compris.

Toute évolution devra cependant préserver les principes fondamentaux du projet :

* la primauté des sources primaires ;
* la traçabilité ;
* la vérifiabilité ;
* la neutralité documentaire ;
* la séparation entre observation et interprétation.

---

# Conclusion

InsouWiki ne cherche pas à produire rapidement du logiciel.

Il cherche à construire durablement une méthode documentaire.

Le code représente l'aboutissement de cette méthode.

Il n'en constitue jamais le point de départ.

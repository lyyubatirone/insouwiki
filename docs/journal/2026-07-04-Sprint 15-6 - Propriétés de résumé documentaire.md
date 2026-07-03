## Sprint 15.6 — Propriétés de résumé documentaire

Ce sprint enrichit `DocumentaryDossier` avec ses premières propriétés calculées de résumé documentaire.

Deux propriétés ont été ajoutées :

* `piece_count`, qui indique le nombre de pièces documentaires contenues dans le dossier ;
* `document_count`, qui indique le nombre de documents distincts représentés dans le dossier.

Ces informations sont calculées à partir des pièces documentaires existantes. Elles ne sont pas stockées séparément, ce qui évite toute duplication et garantit que le résumé reste cohérent avec le contenu réel du dossier.

Cette évolution marque un premier pas vers un résumé documentaire objectif du dossier, sans synthèse ni interprétation.

**Résultat : 55 tests verts.**

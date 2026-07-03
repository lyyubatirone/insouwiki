## Sprint 15.4 — Ordre documentaire par défaut

Ce sprint introduit la première règle documentaire exécutable du moteur de vérification.

Par défaut, un dossier documentaire présente ses pièces de la plus récente à la plus ancienne.

Cette règle est appliquée dans `SimpleDocumentaryDossierBuilder`, qui ordonne désormais les `DocumentaryPiece` selon leur date de publication avant de construire le `DocumentaryDossier`.

L'index documentaire conserve sa responsabilité stricte : il retrouve les pièces, mais ne les classe pas. Le classement par défaut appartient à la construction du dossier documentaire.

Cette évolution reste objective, déterministe et conforme à l'éthique d'InsouWiki : le logiciel facilite la consultation sans interpréter l'importance des pièces.

**Résultat : 53 tests verts.**

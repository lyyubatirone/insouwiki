## Sprint 15.2 — Première implémentation du moteur de vérification documentaire

Ce sprint introduit `SimpleVerificationService`, première implémentation du contrat `VerificationService`.

Le service orchestre désormais les composants du moteur de vérification documentaire :

* réception d'une `VerificationRequest` ;
* interrogation du `DocumentaryIndex` ;
* récupération des `DocumentaryPiece` ;
* construction d'un `DocumentaryDossier` par le `DocumentaryDossierBuilder`.

Cette première implémentation reste volontairement simple. Elle ne contient aucune logique documentaire propre et se limite à coordonner les composants spécialisés.

Cette approche confirme le principe architectural adopté par InsouWiki :

* les composants spécialisés réalisent chacun une responsabilité unique ;
* les services d'orchestration coordonnent ces composants sans réimplémenter leur logique.

Le premier parcours complet du moteur de vérification documentaire est désormais opérationnel :

```text
VerificationRequest
        ↓
DocumentaryIndex
        ↓
DocumentaryPiece
        ↓
DocumentaryDossierBuilder
        ↓
DocumentaryDossier
```

Cette étape marque la fin du MVP du moteur de vérification documentaire. Les prochains développements porteront principalement sur l'amélioration progressive des composants existants, notamment l'index documentaire, sans remettre en cause l'architecture générale.

**Résultat : 52 tests verts.**

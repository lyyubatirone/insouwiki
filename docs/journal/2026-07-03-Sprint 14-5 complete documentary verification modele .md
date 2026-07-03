Sprint 14.5 — Complete documentary verification model

Au cours de ce sprint, le modèle du moteur de vérification documentaire a été complété avec l'introduction de VerificationRequest.

Cette nouvelle classe représente le point d'entrée du moteur de vérification. Elle modélise la demande formulée par un lecteur souhaitant vérifier une affirmation ou ouvrir un dossier documentaire à partir des sources primaires.

Conformément aux principes du projet, VerificationRequest reste volontairement minimaliste et ne contient actuellement qu'une requête textuelle. Les critères de recherche, filtres, préférences d'affichage ou de tri ne font pas partie de la demande elle-même et seront traités ultérieurement par des composants spécialisés.

L'introduction de cet objet complète désormais le parcours conceptuel du moteur de vérification documentaire :

Le lecteur
        ↓
VerificationRequest
        ↓
VerificationService
        ↓
DocumentaryPieceBuilder
        ↓
DocumentaryPiece
        ↓
DocumentaryDossierBuilder
        ↓
DocumentaryDossier
        ↓
Le lecteur vérifie

À l'issue de ce sprint, le modèle conceptuel du moteur de vérification documentaire est désormais complet. Les prochains développements porteront principalement sur l'orchestration des composants existants afin de produire les premiers dossiers documentaires complets.
Sprint 46 – Premier filtrage documentaire

Création de InMemoryDocumentaryRepository, première implémentation du port DocumentaryRepository.
Le repository établit un inventaire documentaire à partir d'une exploration.
Première règle documentaire implémentée : filtrage par auteur.
Les tests valident désormais qu'une exploration contenant le critère Auteur = Jean-Luc Mélenchon produit un inventaire ne contenant que les documents correspondants.
96 tests verts.
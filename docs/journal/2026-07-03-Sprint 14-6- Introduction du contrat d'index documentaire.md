## Sprint 14.6 — Introduction du contrat d'index documentaire

Ce sprint introduit le contrat du futur index documentaire.

`DocumentaryIndex` représente le composant chargé de retrouver les pièces documentaires correspondant à une demande de vérification documentaire.

Cette étape confirme une séparation importante du moteur de vérification :

* les pièces documentaires sont préparées en amont ;
* l'index documentaire les retrouve à partir d'une demande ;
* le moteur de vérification les assemblera ensuite dans un dossier documentaire.

Aucune implémentation concrète de l'index n'a encore été introduite. Le stockage et les modalités de recherche des pièces documentaires restent volontairement ouverts.

La suite de tests reste entièrement valide.

**Résultat : 50 tests verts.**

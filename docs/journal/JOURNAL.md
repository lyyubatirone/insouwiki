Sprint 47 – Intervalle documentaire de dates



Le domaine documentaire s'enrichit d'un nouvel objet de valeur : DocumentaryDateRange.



Cet objet représente un intervalle de dates utilisé pour préciser une exploration documentaire.



Aucune logique métier n'y est encore attachée ; il enrichit simplement le langage du domaine et préparera les futurs critères temporels.



97 tests verts.



100ᵉ test — Premier parcours documentaire complet

Une question documentaire peut désormais donner naissance à une exploration progressivement raffinée par un critère d’auteur puis par un intervalle de dates. Le repository mémoire applique cumulativement ces critères et établit l’inventaire documentaire correspondant.

100 tests verts.



Sprint 51 — Retrait d’un critère documentaire

Une exploration documentaire peut désormais être affinée par l’ajout de critères, puis élargie à nouveau par le retrait d’un critère précis. Les explorations restent immuables : chaque opération produit un nouvel état sans modifier le précédent.

101 tests verts.



Naissance de l'état d'enquête documentaire (InvestigationState). Une enquête devient un objet persistant, partageable et indépendant de son résultat courant.



Les premiers documents découverts avant l'introduction de published\_at nécessiteront un enrichissement documentaire ultérieur.


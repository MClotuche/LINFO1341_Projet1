# Organisation

## TODO
- [x] Découvrir les fonctionalités de OneDrive
    - [ ] Décider des fonctionalités à analyse
- Pour chaque fonctionalité:
    - [ ] Défnir le script/séquence d'actions à réaliser pour tester la fonctionalité
        - [ ] Nécéssite de comprendre les exemples d'anlyses données dans l'énoncé du projet
    - [ ] Exécuter le script/analyse dans les conditions suivantes: Wifi, Ethernet, 4G (autres?)
    - [ ] Réaliser l'analyse de la capture/traces réseau (dépend de chaque fonctionalité)
        - [ ] Graphiques potentiels
        - [ ] Statistiques potentielles avec <code>pyshark</code>

## Timeline
- [ ] S5: Tous les scripts terminés
- [ ] S6: Réalisation des tests et 1ères analyses
- [ ] S7: Analyses et début rapport
- [ ] S8: Rapport

# Fonctionalités de OneDrive
Idée: créer nos répertoires, fichiers, dans ce dépôt git et toujours faire les tests avec eux. \
## Liste choisie
Voir si maj nécéssaire
1. Ouverture de l'application (la base)
2. Connexions à son compte / déconnexion
3. Ouverture d'une section/répertoire
4. Recherche/Filtrage de document
5. Upload
    - fichier
    - dossier
    - Création word directe
6. Download
    - Aperçu / Ouverture d'un fichier
    - Téléchargement d'un fichier
    - Supression
7. Fichiers en général
    - Déplacement
    - Renommer
    - Copier
    - Historique des versions (important)
    - ajouter favoris
8. Partage
    - Partager un document (avec et sans autorisations)
    - Modification simultanée d'un document par plusieurs personnes
    - 
### Liste exhaustive
1. Ouverture de l'application - 
1. Connections
    - Se connecter à onedrive
    - Se déconnecter de Onedrive
1. Ouvrir un document dans la section "Pour vous"
2. Filtrer les documents "Récents" (Par type - nom - personne) - je ne pense pas que ça utilise le réseau
3. Mes fichiers -> trier
4. Ouverture des sections (hypothèse: idem pdv réseau)
    - Mes fichiers
    - Partager
    - Favoris
    - Corbeille
5. Parcourir les fichiers par
    - Personnes
    - Réunions
6. Ajouter
    - Dossier
    - Télécharger un fichier
    - Télécharger un dossier
    - Création d'un nouveau document (Word, Excel...)
    - Ajout d'un lien vers un fichier/page web
7. Pour un fichier / dossier:
    - Ouvrir
    - Aperçu
    - Gérer accès
    - Supprimer
    - Télécharger
    - Ajouter un raccourci
    - Renommer
    - Déplacer vers
    - Copier dans
    - Ouvrir l'historique des versions
         - Restaurer une version
    - Ouvrir les détails
    - Ouvrir l'emplacement
    - Partager (IMPORTANT)
        - Recherche de qqn
        - En ayant les autorisations
        - Sans autorisations -> dmd au propriétaire
    - Ajouter aux favoris
    - Demander des fichiers (DOSSIER)
    - Ouvir un dossier (DOSSIER)
    - Ouvrir un dossier d'un autre propriétaire
8. Généralités (IMPORTANT)
    - Différence entre transfert nouveaux fichiers % modification de fichiers existant
    - Impact de la modification par plusieurs utilisateurs par rapport à 1 seul
    - Volume de données échangées par app pour chaque foncionalité (graphe?)
    - Serveurs relais pour interagir avec un utilisatueur ou communication directe entre applications? Idem si deux users sur le même réseau wifi?
    - Interagir avec user sur même wifi/ethernet a un impact sur la façon dont le trafic applicatif est transporté? serveurs relais?
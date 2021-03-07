# QR_code_renamer

Script python renommant les photos des objets inventoriés et ajoute son URL dans le champs ad-hoc du tableur contenant l'inventaire.
Lors de la première connexion, une URL s'affichera. Cliquer dessus pour ensuite octroyer les droits à l'application

Dépendances :

* OpenCV ;
* google-api-python-client ;
* google-auth-httplib2 ;
* google-auth-oauthlib.

Pour activer la Google Drive API :

* https://console.developers.google.com/flows/enableapi?apiid=drive
* S'assurer que __Créer un projet__ soit sélectionné
* Cliquer sur __Continuer__
* Cliquer sur __Passer à l'étape "Identifiants"__
* Choisir __Google Drive API__
* Choisir __Autre Plateforme avec interface utilisateur__
* Cliquer sur __Données utilisateur__
* Cliquer sur __De quels identifiants ai-je besoin ?__
* Cliquer sur __Configurer l'écran de configuration__
* Pour le User Type, je ne choisis rien et clique sur __Créer__
* Donner un nom au projet
* Choisir une adresse courriel
* Ajouter l'adresse du développeur
* Cliquer sur __Ajouter ou supprimer des niveaux d'accès__
  * Activer le champ d'application __.../auth/drive.appdata__ ;
  * Activer le champ d'application __.../auth/drive.install__ ;
  * Activer le champ d'application __.../auth/drive.file__ ;
  * Activer le champ d'application __.../auth/docs__ ;
  * Activer le champ d'application __.../auth/drive__ ;
* Cliquer sur __Mettre à jour__
* Cliquer sur __Enregistrer et Continuer__
* Cliquer sur __+ Add Users__
* Ajouter l'adresse courriel et cliquer sur __Ajouter__
* Cliquer sur __Enregistrer et Continuer__
* Sur le flanc gauche, cliquer sur __Identifiants__
* Cliquer sur __+ Créer des identifiants__
* Cliquer sur __Id client OAuth__
* Choisir __Application de bureau__
* Donner un nom
* Cliquer sur __Créer__
* Cliquer sur __OK__
* Au niveau de l'identifiant nouvellement créé, cliquer sur la flèche vers le bas pour télécharger

Pour activer la Google Sheets API :

* Ouvrir son projet dans [la console API](https://github.com/museebolo/qr_code_renamer)
* Cliquer sur __Bibliothèque__
* Choisir __Google Sheets API__
* Cliquer sur __Activer__
* Créer un identifiant en cliquant sur __Identifiants__
* Cliquer sur __Ajouter ou supprimer des niveaux d'accès__
  * Activer le champ d'application __.../auth/spreadsheets__ ;
* Cliquer sur __Mettre à jour__
* Cliquer sur __Enregistrer et Continuer__


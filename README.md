# ReseachInternship (ENGLISH AND FRENCH NOTES)

FRENCH:
Repo du projet de stage
Site web dans lequel les utilisateurs peuvent se connecter UNIQUEMENT avec un code d'invitation.
L'administrateur peut envoyer un mail aux utilisateurs, le mail contiendra le code d'invitation.
lorsque l'utilisateur se connecte, le système doit être capable de reconnaître le code
un code ne peut être utilisé qu'UNE SEULE FOIS.

=====================================================
- Mise à jour 26/7/2021 (Application rénovée)
====================================================

Après avoir appris comment fonctionnent les modèles, les rendus, les redirections et les formulaires de Django, j'ai implémenté avec succès la possibilité d'envoyer des invitations par email.
NOTES DE PATCH COMPLÈTES CI-DESSOUS. NOTES D'INSTALLATION ENCORE PLUS LOIN CI-DESSOUS ;
AJOUTÉ :
- Ajout complet de la possibilité d'envoyer des invitations par mail (l'utilisateur doit être connecté pour pouvoir envoyer une invitation). Pour envoyer une invitation, cliquez sur "détails" sous une équipe, puis cliquez sur "inviter des utilisateurs". Vous recevrez un message si l'invitation est réussie.
- La possibilité de modifier le profil (nom, prénom, email et photo) a été ajoutée pour le moment.
- Login/logout fonctionne bien.
- MySQL comme base de données. Pour contourner un problème initial existant
- Ajout d'un peu de ViewJS
SUPPRIMÉ :
- L'ancien design pour le moment. Sera ajouté bientôt, petit à petit
Autres mentions :
- La barre de navigation de connexion a été supprimée pour les utilisateurs qui ne sont pas encore connectés. Elle sera ajoutée prochainement. Mais je voulais juste tester une future fonctionnalité
- le fait que TOUTE PERSONNE connectée puisse créer une équipe sera restreint. Les équipes sont comme des "départements" dans lesquels il ne peut y avoir qu'un seul créateur et administrateur de département.
- Quelques trucs ne fonctionnent pas encore. A corriger très bientôt.
Choses à ajouter dans le futur :
- Possibilité pour les invités de supprimer des utilisateurs.
- Possibilité pour les utilisateurs de poster des articles sur la page d'accueil (simplement des images pour le moment).
- Autres détails mineurs
Pour accéder manuellement au login, tapez "http://127.0.0.1:8000/login/".
Procédure d'installation :
1.	Cloner/fork le projet
2.	Activez l'environnement virtuel (env) en utilisant le terminal
3.	Installer Django
4.	Installer pillow, installer mysqlclient
a.	EDITER LA BASE DE DONNEES dans invitations/settings.py à ce qui correspond à votre goût : mysql, postgre, sqlite etc... (IMPORTANT !). Dans mon cas, c'est MySQL qui a été utilisé.
b.	EDITER LA CONFIGURATION SMTP dans invitations/settings.py avec ce qui vous convient. (IMPORTANT !). Dans mon cas, j'ai utilisé Google SMTP. 
5.	Faire les migrations, migrer
6.	Créer un superutilisateur
7.	Exécuter le serveur. NE PAS OUVRIR LE PROJET.
8.	Parcourez les tables de votre base de données, allez à la table "userprofile_userprofile". Insérez un nouveau profil utilisateur en choisissant l'id du super utilisateur que vous avez créé. C'EST TOUT. C'est parce que le super-utilisateur n'a pas de profil d'utilisateur lorsqu'il est créé. Il est donc impossible d'utiliser l'application correctement. Cette étape n'est requise qu'une seule fois
9.	Ouvrez un nouvel onglet et connectez-vous au projet via http://127.0.0.1:8000/login/.
10.	Ajoutez une nouvelle équipe
11.	Invitez des utilisateurs 
12.	Testez l'application !


Plus de mises à jour à venir ! 

ENGLISH:
Internship Project Repo
Website in which Users Can login ONLY with an invitation code.
Admin Can send a mail to users , the mail wil contain the said invitation code
when the user logs in, the system should be able to recognize the code
a code can be used only ONCE.

=================================================================
-------------Update 26/7/2021 (Application Revamped)------------
==================================================================
After learning how Django Models, renders, redirections and forms work, I successfully implemented the ability to send invitations via email.

FULL PATCH NOTES BELOW. INSTALLATION NOTES EVEN FURTHER BELOW;
ADDED:
-	Fully Added ability to send invite via mail (user must be logged in order to be able to send an invite). To send an invite, click on “details” under any team, then click “invite users”. You will get a message if successful.
-	Fully added the ability to edit profile (first, last name, email and profile picture) for now.
-	Login/logout works well.
-	MySQL as DataBase. To work around an initial issue existing
-	Added a bit of ViewJS

REMOVED:
-	The old design for now. Will be added soon, bit by bit
Other mentions:
-	The login navbar has been removed for users who aren’t logged in yet. This will be added next. But I just wanted to test a future feature
-	the fact that ANYONE logged in can create a team will be restricted. Teams are like “departments" in which there can be only 1 department creator and admin.
-	Some few stuffs don’t work yet. To be fixed very soon.

Things to be added in future:
-	Ability for inviter to remove users.
-	Ability for users to post articles in the front page (simply images for now)
-	Other minor details

To manually access the login type in “http://127.0.0.1:8000/login/"
Installation procedure:
1.	Clone/fork project
2.	Activate virtual environment (env) using terminal
3.	Install Django
4.	Install pillow, install mysqlclient
        a.	EDIT THE DATABASE in invitations/settings.py to whatever corresponds your liking: mysql, postgre, sqlite etc… (IMPORTANT!). In my case, MySQL was used.
        b.	EDIT THE SMTP CONFIGURATION in invitations/settings.py to whatever goes for you. (IMPORTANT!). In my case, Google SMTP was used. 
5.	Make migrations, migrate
6.	Create superuser
7.	Run server. DO NOT OPEN PROJECT.
8.	Browse your database tables go to “userprofile_userprofile” table. Insert new userprofile by choosing your created superuser id. THAT’S ALL. This is because, the superuser does not have a userprofile when it is created. So, it makes it impossible to use the app properly. This step is required only once
9.	Open a new tab and login to the project through http://127.0.0.1:8000/login/
10.	Add a new team
11.	Invite users 
12.	Test the app!



More updates coming soon! 


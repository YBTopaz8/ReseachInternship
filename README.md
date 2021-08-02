# ReseachInternship (ENGLISH AND FRENCH NOTES)

FRENCH:

Repo du projet de stage
Site web dans lequel les utilisateurs peuvent se connecter UNIQUEMENT avec un code d'invitation.
L'administrateur peut envoyer un mail aux utilisateurs, le mail contiendra le code d'invitation.
lorsque l'utilisateur se connecte, le système doit être capable de reconnaître le code
un code ne peut être utilisé qu'UNE SEULE FOIS.

================================================================================
- Mise à jour 02/8/2021 (Fonctionnalités utilisateur implémentées)
================================================================================

Après la mise à jour précédente, je me suis concentré un peu plus sur l'apprentissage des modèles/fichiers statiques et des URLs. Je n'ai pas encore saisi tout le concept, mais j'ai acquis suffisamment de connaissances pour être capable d'implémenter une forme basique d'expérience utilisateur. Comme expliqué ci-dessous.
Le Changelog complet est affiché ci-dessous ; 
(aussi)Les NOTES D'INSTALLATION SONT PLUS LOIN AU-DESSOUS, donc assurez-vous de les suivre fidèlement afin d'être prêt à utiliser le système ;
Ajouté :
- Application "Articles" : qui est l'application qui gère tout ce qui concerne les articles (ajout/modification/suppression).
- Les utilisateurs peuvent ajouter un article après s'être connectés
- Ils peuvent également modifier et supprimer l'article facilement
- Un aperçu rapide des articles en page d'accueil, qui peuvent être triés par leur catégorie (ils sont seulement visibles pour le moment. En cliquant dessus, aucun effet ne sera obtenu pour le moment. Je vais travailler dessus très bientôt)
- Ajout de la barre de connexion même pour les utilisateurs non connectés, afin qu'ils puissent facilement cliquer pour se connecter, plutôt que de taper des urls. Si vous n'avez pas de compte et que vous cliquez sur "Signup", vous serez invité à écrire votre code d'invitation avant de continuer.
Supprimé :
- La possibilité pour TOUT utilisateur de créer une équipe a été supprimée. (ceci parce que le droit de créer une équipe devrait être réservé aux chefs d'équipe nommables).
- La possibilité pour TOUT utilisateur d'inviter des personnes à une équipe a également été supprimée, avec le même raisonnement que le précédent.
- La possibilité pour un utilisateur d'appartenir à différentes équipes a été supprimée pour le moment. Principalement pour des raisons de simplicité. Elle peut être réintroduite si nécessaire.
- Autres minorités
Autres mentions :
- La page d'accueil s'appelle "frontpage1.html" elle est actuellement utilisée à des fins de développement et de tests. Quand tout sera clair, tout sera déplacé vers "frontpage.html". 
- L'option "inviter un utilisateur" dans la page "myaccount" fonctionne maintenant comme prévu.
Autres choses que j'ai pu oublier 😅


Plus de mises à jour à venir ! 

===================================================================================================================

ENGLISH:

================================================================================
Update 02/8/2021 (User Functionalities implemented)
================================================================================

After the previous, I focused a bit more on learning about models/static files and URLs. I haven’t grasped the whole concept, but I have acquired enough knowledge to be able to implement a BASIC form of user experience. As explained below.
Full Changelog, INSTALLATION NOTES EVEN FURTHER BELOW, so endeavor to follow them keenly in order to be able to be good to go;
Added:
-	“Articles” application: which is the app that manages whatever concerns Articles (addition/edit/deletion).
-	Users can successfully add an article after login
-	They can also edit and delete the article easily
-	A quick overview of the articles in frontpage, that can be sorted by their category (they are only viewable for now. Clicking on them won’t do anything just yet. I’ll be working on them soon enough)
-	Added the login bar even for non-logged user, so they can easily click to login, rather than typing urls. If you don’t have an account and click on signup, you will be prompted to write your invitation code first before continuining
Removed:
-	The ability for ANY user to create a team was removed. (this is so because the right to create a team should be reserved to appointable team leaders)
-	The ability for ANY user to invite people to a team has also been removed, with the same reasoning as the previous in mind.
-	The ability for one user to belong to different teams has been removed for now. Mostly for the sake of simplicity. It can be brought back if need be.
-	Other minorities
Other Mentions:
-	The frontpage is called “frontpage1.html” it is currently being used for development purposes and tests. When clear, everything will be moved back to “frontpage.html” 
-	The “invite user” in “myaccount” page now works as intended.
Other things I might have forgotten 😅

More updates coming soon! 


------------------------------------------------------------------------------------------------------------------------------------------------------
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
9.	Ouvrez un nouvel onglet et connectez-vous au projet 
10.	Ajoutez une nouvelle équipe
11.	Invitez des utilisateurs 
12.	Testez l'application !


Plus de mises à jour à venir ! 

===================================================================================================================
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
9.	Open a new tab and login to the project 
10.	Add a new team
11.	Invite users 
12.	Test the app!



More updates coming soon! 


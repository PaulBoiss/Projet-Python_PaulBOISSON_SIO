# Introduction
Bienvenue sur mon API de gestion de fichiers, réalisée en tant que projet du module "Data Intensive Python 2020". Cette API, codée sous Python (3.8.6) permet de stocker des vignettes d'images aux formats .jpeg, .jpg, .png ou .gif, de les afficher et de récupérer leurs métadonnées.  Dans le cadre de ce projet, les vignettes sont stockées localement, dans le dossier static/uploads. Le programme est livré avec un dossier Banque_Images qui contient des fichiers utilisables pour essayer l'application. 


# Pré-requis
Cette API utilise différentes librairies précisées dans le fichier "Requirements". Pour installer ces librairies, on utilise PIP, l'installateur de paquets Python, qui est fourni par défaut avec les version de Python 3 supérieures à la version 3.4. 

Installation de Flask pour la création de serveur web:
&rarr; python3 -m pip install flask

Installation de Pillow pour la gestion des images:
&rarr; python3 -m pip install --upgrade Pillow

Installation de Pytest pour lancer le script de tests:
&rarr; python3 -m pip install -U pytest

Installation de Requests pour effectuer des requêtes à l'API directement avec Python:
&rarr; python3 -m pip install requests

# Lancement du serveur
L'application est hébergée sur un serveur Flask, qui peut être lancé avec la commande suivante:  
&rarr; FLASK_APP=main.py flask run
ou
&rarr; python3 -m main.py
ou
&rarr; python3 -m main

L'application sera hébergée localement est accessible à l'url "http://localhost:5000/".

Flask utilise le port 5000 par défaut. Ce port peut être déjà utilisé par une autre application. Il peut être judicieux de tuer ces programmes.  

Lister les programme en écoute :  
&rarr; sudo lsof -i -P -n | grep LISTEN  

Tuer les programme sur le port 5000:  
&rarr; sudo fuser -k 5000/tcp

# Description de l'application
Pour accéder à l'application rendez-vous à l'url "http://localhost:5000/" sur un navigateur web (Google Chrome, Firefox, Safari ou autre). Une interface graphique a été créée afin de faciliter l'utilisation de l'API et son fonctionnement est limpide. Il est toutefois possible de ne passer que par des lignes de commande et faire des requêtes en utilisant la commande curl. Cette dernière méthode ne permet de charger que des images déjà présentes dans le dossier Banque_Images.  

Les images du dossier Banque_Images sont les suivantes:
- Adobe.png
- Ajax.png
- Apache.png
- jquery.gif
- linux.svg
- Sujet_Projet.pdf
- text.docx
- web.jpg  

Référez-vous à cette liste si vous souhaitez charger une image en utilisant la ligne de commande. Vous n'êtes pas limité à cette liste si vous passez par l'interface graphique. 


# Fonctionnalités
Voici les différentes fonctionnalités:

## Importer une image:
Via l'interface graphique:  
- Cliquez sur "Parcourir", et sélectionnez une image (des images sont disponibles dans le dossier "Banque_Images" )  
- Cliquez sur "Envoyer"

Via la ligne de commande:  
        &rarr; curl http://127.0.0.1:5000/load_com/<nom_image.extension>  

A l'issue de cette opération, quatre messages différents peuvent vous être renvoyés sur l'interface graphique:  
        &rarr; Si l'image existe déjà : *'Image déjà chargée'*  
        &rarr; Si l'image ne contient pas de donnée: *'Pas de partie fichier'*  
        &rarr; Si aucune image n'est sélectionnée: *'Aucune image sélectionnée'*  
        &rarr; Si le format du fichier n'est pas accepté: *'Ce format d image n est pas autorisé. Veuillez utiliser les formats suivants: png, jpg, jpeg, gif'*  
        &rarr; Si l'image a correctement été importée: *'Image correctement chargée et affichée'*  


## Voir la liste des images chargées
Via l'interface graphique:  
    Vous pouvez observer directement les vignettes des images déjà chargées. 

Via la ligne de commande:  
    &rarr; curl http://localhost:5000/liste_com


## Afficher la vignette d'une image:
Via l'interface graphique:  
- Cliquez directement sur une des images qui est apparu sur l'interface  

Via la ligne de commande:  
&rarr; curl http://localhost:5000/display_com/<nom_image.extension>  



## Afficher les métadonnées d'une image:  
Via l'interface graphique:  
- Cliquez sur le bouton "Metadata" en face d'une des images  

Via la ligne de commande:  
&rarr; curl http://localhost:5000/metadata/<nom_image.extension>  
Attention, il n'y a pas de "_com" pour celui-ci.  


## Supprimer une image du serveur:
Via l'interface graphique:
- Cliquez sur le bouton "Supprimer" en face d'une des images

Via la ligne de commande:  
&rarr; curl http://localhost:5000/removeFile_com/<nom_image.extension>

# Lancement du script de tests
Pour lancer le script de test, rendez-vous dans le dossier,du projet /PROJETPYTHON_PAULBOISSON_SIO/Projet avec un terminal et lancez Pytest à l'aide de la commande  
&rarr; pytest -s  
ou  
&rarr; python3 -m pytest -s (sur Windows)

Le script sera exécuté et des print() ont été utilisés pour détailler les tests. 

Elements testés :
- Connexion à la page web
- Ajout d'une image "Adobe.png" depuis le dossier "Banque_Images"
- Ajout d'un fichier pdf "Sujet_Projet.pdf" depuis le dossier "Banque_Images"
- Affichage d'une image
- Correspondance des métadonnées de l'image "Adobe.png" avec son nom
- Suppression de l'image "Adobe.png"

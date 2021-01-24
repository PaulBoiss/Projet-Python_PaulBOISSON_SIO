import os
from app import app, url, exampleFolder
import urllib.request
from flask import Flask, flash, request, redirect, url_for, render_template, send_from_directory
from werkzeug.utils import secure_filename
import PIL.Image
import PIL.ImageTk
from tkinter import Tk, Label
import requests
import json


# Fonction de sécurisation des images
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])
def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


# Route de connection à l'application (affichage des images déjà chargées)
@app.route('/', methods=['GET'])
def webPage():
	files = os.listdir(app.config['UPLOAD_FOLDER']) 
	return render_template('upload.html', files=files) 

# Liste des fichiers chargés (ligne de commande)
@app.route('/liste_com', methods=['GET'])
def listImages():
	liste = ''
	files = os.listdir(app.config['UPLOAD_FOLDER']) 
	for file in files:
		liste = liste + '     '+ file
    liste += ' \n '
	return(liste)


# Route de sélection d'une image (ligne de commande)
@app.route('/load_com/<picture>',methods=['GET'])
def load_image(picture):
	if not os.path.exists(exampleFolder + picture):
		return "Cette image n'existe pas dans le dossier Banque_Images \n "
	if os.path.exists(app.config['UPLOAD_FOLDER']+ picture):
		return 'Image déjà chargée \n '
	if picture == '':
		return 'Aucune image sélectionnée \n '
	else:
		try:
			file = PIL.Image.open(exampleFolder+picture)
		except:
			return "Ce format d'image n'est pas autorisé. Veuillez utiliser les formats suivants: png, jpg, jpeg, gif \n "
		else:
			if file and allowed_file(picture):
				filename = secure_filename(picture)
				file.thumbnail((400, 400))
				file.save(app.config['UPLOAD_FOLDER']+filename)
				return 'Image correctement chargée \n '
			else:
				return "Ce format d'image n'est pas autorisé. Veuillez utiliser les formats suivants: png, jpg, jpeg, gif \n "


# Route de chargement d'une image
@app.route('/', methods=['POST'])
def upload_image():
	if 'file' not in request.files:
		flash('Pas de partie fichier \n ')
		return redirect(request.url)
	file = request.files['file'] 
	if os.path.isfile(os.path.join(app.config['UPLOAD_FOLDER'], file.filename)):
		flash('Image déjà chargée \n ')
		return redirect(request.url)
	if file.filename == '':
		flash('Aucune image sélectionnée \n ')
		return redirect(request.url)
	if file and allowed_file(file.filename):
		filename = secure_filename(file.filename)
		img=PIL.Image.open(file)
		img.thumbnail((400, 400))
		img.save(os.path.join(app.config['UPLOAD_FOLDER'], filename)) 
		flash('Image correctement chargée et affichée') 
		return redirect(request.url)
	else:
		flash("Ce format d'image n est pas autorisé. Veuillez utiliser les formats suivants: png, jpg, jpeg, gif \n ")
		return redirect(request.url)
 
# Route pour afficher un des fichier en grand
@app.route('/display/<filename>',methods=['GET'])
def display_image(filename):
	return redirect(url_for('static', filename='uploads/' + filename), code=301)
 
# Route pour afficher un des fichier en grand (ligne de commande)
@app.route('/display_com/<filename>',methods=['GET'])
def display_imageTk(filename):
	try:
   		load = PIL.Image.open(app.config['UPLOAD_FOLDER']+filename)
	except:
		return "Le fichier n'existe pas \n"
	else:
		root = Tk()
		root.title("Vignette "+filename)
		root.geometry("550x450")
		photo = PIL.ImageTk.PhotoImage(load)
		label_img = Label(root, image = photo)
		label_img.place(x=0, y=0)
		root.mainloop()
		return "Image affichée \n "


# Route pour supprimer un fichier du stockage
@app.route('/removeFile/<filename>')
def removeFile(filename):
	try:
   		os.remove(app.config['UPLOAD_FOLDER']+filename)
	except:
		flash('le fichier n existe pas \n ')
		return redirect(url_for('webPage'))
	else:
		return redirect(url_for('webPage'))

# Route pour supprimer un fichier du stockage (ligne de commande) 
@app.route('/removeFile_com/<filename>')
def removeFileCom(filename):
	try:
   		os.remove(app.config['UPLOAD_FOLDER']+filename)
	except:
		return "Le fichier n'existe pas \n "
	else:
		return "Fichier parfaitement supprimé \n "


# Route pour obtenir les metadonnées d'une des images
@app.route('/metadata/<filename>')
def seeMetadata(filename):
	try:
		img = PIL.Image.open(app.config['UPLOAD_FOLDER']+ filename)
	except:
		return "Le fichier n'existe pas \n "
	else:
		return(json.dumps({'Nom':filename.rsplit('.', 1)[0].lower(), 'Format':img.format, 'Dimensions':img.size},indent=4))


# Lancement de l'application à l'execution du script
if __name__ == "__main__":
    app.run(debug=True)
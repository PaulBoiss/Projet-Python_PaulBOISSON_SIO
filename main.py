import os
from app import app
import urllib.request
from flask import Flask, flash, request, redirect, url_for, render_template, send_from_directory
from werkzeug.utils import secure_filename

from PIL import Image

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

# Route de chargement d'une image
@app.route('/', methods=['POST'])
def upload_image():
	if 'file' not in request.files:
		flash('No file part')
		return redirect(request.url)
	file = request.files['file'] 
	if os.path.isfile(os.path.join(app.config['UPLOAD_FOLDER'], file.filename)):
		flash('Image déjà chargée')
		return redirect(request.url)
	if file.filename == '':
		flash('Aucune image sélectionnée')
		return redirect(request.url)
	if file and allowed_file(file.filename):
		filename = secure_filename(file.filename)
		img=Image.open(file)
		print('La taille de l image est :', img.size)
		img.thumbnail((400, 400)) # Redimensionnement de l'image
		print('Maintenant la taille de l image est :',img.size)
		img.save(os.path.join(app.config['UPLOAD_FOLDER'], filename)) 
		flash('Image correctement chargée et affichée') 
		return redirect(request.url)
	else:
		flash('Ce format d image n est pas autorisé. Veuiller utiliser les formats suivants: png, jpg, jpeg, gif')
		return redirect(request.url)

# Route pour afficher un des fichier en grand
@app.route('/display/<filename>',methods=['GET'])
def display_image(filename):
	return redirect(url_for('static', filename='uploads/' + filename), code=301)

# Route pour supprimer un fichier du stockage
@app.route('/removeFile/<filename>')
def removeFile(filename):
	try:
   		os.remove("./static/uploads/"+filename)
	except:
		flash('le fichier n existe pas')
		return redirect(url_for('webPage'))
	else:
		return redirect(url_for('webPage'))

# Route pour obtenir les metadonnées d'une des images
@app.route('/metadata/<filename>')
def seeMetadata(filename):
	img = Image.open('./static/uploads/'+ filename)
	return(json.dumps({'Nom':filename.rsplit('.', 1)[0].lower(), 'Format':img.format, 'Dimensions':img.size},indent=4))

# Lancement de l'application à l'execution du script
if __name__ == "__main__":
    app.run(debug=True)
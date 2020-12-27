import os
from app import app
import urllib.request
from flask import Flask, flash, request, redirect, url_for, render_template, send_from_directory
from werkzeug.utils import secure_filename

from PIL import Image
from PIL.ExifTags import TAGS

import json

# Cette variable n'est pas un paramètre de l'application car est utilisée dans allowed_file. 
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])
def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Première app.route qui permet de lancer la page html lorsqu'on lance le serveur et qu'on s'y connecte. S'y connecter, c'est une requête GET. 
@app.route('/', methods=['GET'])
def upload_form():
	files = os.listdir(app.config['UPLOAD_FOLDER']) # files devient la liste des fichiers dans le dossier d'upload. 
	return render_template('upload.html', files=files) # On renvoit la page html contenant la liste des fichiers dans le dossier d'upload

# Lorsqu'on appuie sur le bouton submit de la page HTML, celui-ci émet une requête POST. 
@app.route('/', methods=['POST'])
def upload_image():
	if 'file' not in request.files:
		flash('No file part')	# Message flash
		return redirect(request.url)
	file = request.files['file'] # file devient le fichier chargé dans la page html
	if file.filename == '':
		flash('No image selected for uploading') # Message flash
		return redirect(request.url)
	if file and allowed_file(file.filename):
		filename = secure_filename(file.filename) # Il faut sécuriser le nom du fichier pour éviter que des commandes se cachent dedans.  

		# ICI IL FAUT RESIZE L'IMAGE
		
		file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename)) # Ce n'est qu'à partir du moment où on utilise la méthode save que le fichier est enregistré sur le disque 
		flash('Image successfully uploaded and displayed') # Le flash est un élément qui peut être récupéré par la partie html avec jinja2. 
		return redirect(request.url)
	else:
		flash('Allowed image types are -> png, jpg, jpeg, gif')
		return redirect(request.url)

# Cette fonction est déclenchée par l'affichage d'une image dans la partie html. 
@app.route('/display/<filename>',methods=['GET'])
def display_image(filename):
	return redirect(url_for('static', filename='uploads/' + filename), code=301)
	#return redirect(request.url)

@app.route('/uploadedFiles')
def show_list():
	return [os.listdir(app.config['UPLOAD_FOLDER'])]

@app.route('/removeFile/<filename>')
def removeFile(filename):
	try:
   		os.remove("./static/uploads/"+filename)
	except:
		flash('le fichier n existe pas')
		return redirect(url_for('upload_form'))
	else:
		return redirect(url_for('upload_form'))

@app.route('/metadata/<filename>')
def seeMetadata(filename):
	img = Image.open('./static/uploads/'+ filename)
	return(json.dumps({'filename':filename, 'format':img.format, 'size':img.size},indent=4))

if __name__ == "__main__":
    app.run(debug=True)
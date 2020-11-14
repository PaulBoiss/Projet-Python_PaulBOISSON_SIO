from flask import Flask

# --------Détermination du fichier où stocker les images---------
UPLOAD_FOLDER = 'static/uploads/'

# ---------Création de l'application----------
app = Flask(__name__)
app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER # 1)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024 # 2)
# 1) On configure l'appli pour qu'elle ait une variable UPLOAD_FOLDER qui corresponde à celle attribuée précédemment. 
# 2) On créee une variable MAX_CONTENT_LENGTH que l'on utilisera comme la taille maximale autorisée pour une image. 



# -> l'application flask est crée, mais elle ne fait rien pour l'instant. 
import os
from app import url
import requests

# Test connection au site
def test_get_webPage():
    print("------Test de connection à la page------")
    r = requests.get(url)
    print("Aboutissement de la requête (200 si ok):", r.status_code)
    assert r.status_code == 200

def test_upload_image():
    print("------Test d'importation d'une image Adobe.png'------")
    files = {'file':open('../Banque_Images/Adobe.png','rb')}
    r = requests.post(url, files = files)
    print("Aboutissement de la requête (200 si ok):", r.status_code)
    print("Le fichier a-t-il bien été chargé ? (True si ok): ", os.path.exists('./static/uploads/Adobe.png'))
    assert r.status_code == 200

def test_mauvais_fichier():
    print("------Test importation d'un fichier Sujet_Projet.pdf------")
    files = {'file':open('../Banque_Images/Sujet_Projet.pdf','rb')}
    r = requests.post(url, files = files)
    print("Aboutissement de la requête (200 si ok):", r.status_code)
    print("Mauvais format importé ? (False si ok): ", os.path.exists('./static/uploads/Sujet_Projet.pdf'))
    assert r.status_code == 200 and os.path.exists('./static/uploads/Sujet_Projet.pdf') == False

def test_display_image():
    r = requests.get(url+'display/Adobe.png')
    assert r.status_code == 200

def test_seeMetadata():
    print("------Test de récupération des métadonnées du fichier Adobe.png------")
    r = requests.get(url+'metadata/Adobe.png')
    rep = r.json()
    print("Récupération du nom du fichier (adobe si ok):",rep["Nom"])
    assert rep["Nom"] == 'adobe'

def test_removeFile():
    print("------Test de suppression d'un fichier Sujet_Projet.pdf------")
    r = requests.get(url+'removeFile/Adobe.png')
    print("Aboutissement de la requête (200 si ok):", r.status_code)
    print('Le fichier est-il toujours dans le dossier ? (False si ok) :', os.path.exists('./static/uploads/Adobe.png'))
    assert r.status_code == 200 and os.path.exists('./static/uploads/Adobe.png') == False

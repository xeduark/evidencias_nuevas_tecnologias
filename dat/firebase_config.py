import os
import firebase_admin
from firebase_admin import credentials, firestore

# Cargar las credenciales desde las variables de entorno
cred_data = {
    "type": os.getenv('firebase_type'),
    "project_id": os.getenv('firebase_project_id'),
    "private_key_id": os.getenv('firebase_private_key_id'),
    "private_key": os.getenv('firebase_private_key').replace('\\n', '\n'),
    "client_email": os.getenv('firebase_client_email'),
    "client_id": os.getenv('firebase_client_id'),
    "auth_uri": os.getenv('firebase_auth_uri'),
    "token_uri": os.getenv('firebase_token_uri'),
    "auth_provider_x509_cert_url": os.getenv('firebase_auth_provider_x509_cert_url'),
    "client_x509_cert_url": os.getenv('firebase_client_x509_cert_url')
}

# Inicializar Firebase con las credenciales
cred = credentials.Certificate(cred_data)
firebase_admin.initialize_app(cred)

db = firestore.client()

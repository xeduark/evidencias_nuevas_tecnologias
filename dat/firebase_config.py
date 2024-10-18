import toml
import firebase_admin
from firebase_admin import credentials, firestore

# Leer el archivo secrets.toml y convertirlo en un diccionario
config = toml.load('secrets.toml')

# Convertir los datos de Firebase en un diccionario para facilitar el acceso
firebase_config = config.get('firebase', {})

# Verificar que todos los campos necesarios estén presentes
required_fields = [
    'type', 'project_id', 'private_key_id', 'private_key', 
    'client_email', 'client_id', 'auth_uri', 
    'token_uri', 'auth_provider_x509_cert_url', 'client_x509_cert_url'
]

# Usar una estructura condicional para validar las credenciales
if all(field in firebase_config for field in required_fields):
    # Si todos los campos están presentes, crear el diccionario de credenciales
    cred_data = {field: firebase_config[field] for field in required_fields}

    # Inicializar Firebase con las credenciales
    cred = credentials.Certificate(cred_data)
    firebase_admin.initialize_app(cred)

    db = firestore.client()
    print("Firebase inicializado correctamente.")
else:
    missing_fields = [field for field in required_fields if field not in firebase_config]
    print(f"Faltan los siguientes campos en las credenciales: {missing_fields}")

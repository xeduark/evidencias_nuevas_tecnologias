import firebase_admin  
from firebase_admin import credentials, firestore  

# Inicializa Firebase
def inicializar_firebase():
    if not firebase_admin._apps:  
        firebase_credentials = st.secrets["firebase"]  
        secrets_dict = firebase_credentials.to_dict()  
        
        try:
            cred = credentials.Certificate(secrets_dict)  
            firebase_admin.initialize_app(cred)
            return firestore.client()  # Devuelve el cliente de Firestore
        except ValueError as e:
            raise RuntimeError(f"Error al inicializar Firebase: {e}")
    return firestore.client()  # Retorna el cliente existente si ya está inicializado

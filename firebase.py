# from firebase import firebase_admin, credentials, database
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db, firestore

def getDataFromDB():
    # Fetch the service account key JSON file contents
    cred = credentials.Certificate('token_key.json')
    # Initialize the app with a service account, granting admin privileges
    firebase_admin.initialize_app(cred)
    db = firestore.client()
    data = db.collection("config").get()
    return data[0].to_dict()


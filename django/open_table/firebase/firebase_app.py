import firebase_admin
from firebase_admin import auth
from firebase_admin import credentials

# Path to your service account key
cred = credentials.Certificate("./serviceAccountKey.json")
firebase_app = firebase_admin.initialize_app(cred)
from flask import Flask
app = Flask(__name__)

import firebase_admin
from firebase_admin import credentials, auth

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

@app.route("/")
def hello():
    return "Hello world!"

@app.route("/register")
def register():
    user = auth.create_user(
        email='user@example.com',
        email_verified=False,
        phone_number='+15555550100',
        password='secretPassword',
        display_name='John Doe',
        photo_url='http://www.example.com/12345678/photo.png',
        disabled=False
    )
    print('Sucessfully created new user: {0}'.format(user.uid))

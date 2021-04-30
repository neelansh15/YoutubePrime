from flask import Flask, request
app = Flask(__name__)

import firebase_admin
from firebase_admin import credentials, auth

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

@app.route("/")
def hello():
    return "Hello world!"

@app.route("/register", methods=["POST"])
def register():
    if request.method == "POST":
        user = auth.create_user(
            email= request.args.get('email', ''),
            password= request.args.get('password', ''),
            display_name=request.args.get('display_name', ''),
            photo_url=request.args.get('photo_url', ''),
            disabled=False,
        )
        print(user)
        print('Sucessfully created new user: {0}'.format(user.uid))
        return user.email
    else:
        print("Only POST method allowed")
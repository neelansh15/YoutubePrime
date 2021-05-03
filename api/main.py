from datetime import datetime, timedelta
from dateutil.tz import gettz
import json

from flask import Flask, request
app = Flask(__name__)

import firebase_admin
from firebase_admin import credentials, auth, storage, firestore
from flask import request

import pyrebase

pyrebaseConfig = {
    "apiKey": "AIzaSyAkGjSyK949IiUwlD3wMjyRrZOb4Um8I9M",
    "authDomain": "prime-43c05.firebaseapp.com",
    "projectId": "prime-43c05",
    "storageBucket": "prime-43c05.appspot.com",
    "messagingSenderId": "236302739370",
    "appId": "1:236302739370:web:ec079001c46176d29bedd3",
    "measurementId": "G-RYD5FJW22L",
    "serviceAccount": "serviceAccountKey.json"
}

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    "storageBucket": "prime-43c05.appspot.com",
})
db = firestore.client()

@app.route("/")
def hello():
    return "Hello world!"

@app.route("/register", methods=["POST"])
def register():
    #TODO: 1) Use RegEx to verify user credentials. 2) Add try catch and return errors
    user_json = request.get_json(force=True)
    user = auth.create_user(
        email= user_json['email'],
        password= user_json['password'],
        display_name=user_json['display_name'],
        photo_url=user_json['photo_url'],
    )
    
    db.collection("users").document(user.uid).set({
        "uid": user.uid,
        "email": user.email,
        "display_name": user.display_name,
        "photo_url": user.photo_url,
        "subscriber_count": 0
    })

    print('Sucessfully created new user: {0} {1}'.format(user.email, user.uid))
    
    access_token = auth.create_custom_token(user.uid)
    return access_token

@app.route("/upload-video", methods=['GET'])
def uploadVideo():
    bucket = storage.bucket()
    blob = bucket.blob("videos/new2.mp4")

    blob.upload_from_filename("E:\\Documents\\Programming\\onlyPrime\\abc.mp4")
    return 'Successful'

@app.route("/download-video", methods=['GET'])
def downloadVideo():
    bucket = storage.bucket()
    blob = bucket.blob("videos/new.mp4")
    
    expiration_time = datetime.now(tz=gettz('Asia/Kolkata')) + timedelta(minutes=1)
    print(expiration_time)

    url = blob.generate_signed_url(expiration=expiration_time, version='v4')
    
    return f"<video src='{url}' width=500 height=500 autoplay></video><input value={url} disabled />"

@app.route("/subscribe", methods=['POST'])
def subscribe():
    # token = request.args.get('accessToken', '')
    # decoded_token = auth.verify_id_token(token)
    # user_uid = decoded_token['uid']
    data = request.get_json()
    user_uid = data['username']
    channel_uid = data['channel_uid']
    channel_doc = {
        "uuid": channel_uid
    }

    db.collection("users").document(user_uid).collection("subscriptions").add(channel_doc)

@app.route("/user", methods=["POST"])
def getUserDetails():

    #TODO: Auth token for security, or add firebase rule to accept an auth header

    reqJSON = request.get_json(force=True)
    uid = reqJSON["uid"]
    # user_record = auth.get_user(uid) NOT REQUIRED

    userDoc = db.collection("users").document(uid).get()
    userDocData = userDoc.to_dict()

    return json.dumps(userDocData)

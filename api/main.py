from datetime import datetime, timedelta
from dateutil.tz import gettz
import json

from flask import Flask, request
app = Flask(__name__)

import firebase_admin
from firebase_admin import credentials, auth, storage , firestore
from flask import request



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
    return user.email

@app.route("/upload-video", methods=['GET'])
def uploadVideo():
    bucket = storage.bucket('prime-43c05.appspot.com')
    blob = bucket.blob("videos/new2.mp4")

    blob.upload_from_filename("E:\\Documents\\Programming\\onlyPrime\\abc.mp4")
    return 'Successful'

@app.route("/download-video", methods=['GET'])
def downloadVideo():
    bucket = storage.bucket()
    blob = bucket.blob("videos/new.mp4")
    
    expiration_time = datetime.now(tz=gettz('Asia/Kolkata'))+ timedelta(minutes=1)
    print(expiration_time)

    url = blob.generate_signed_url(expiration=expiration_time, version='v4')
    
    return f"<video src='{url}' width=500 height=500 autoplay></video><input value={url} disabled />"

# @app.route("/subscribe", methods=['POST'])
# def subscribe():
#     # token = request.args.get('accessToken', '')
#     # decoded_token = auth.verify_id_token(token)
#     # user_uid = decoded_token['uid']
#     user_uid =request.args.get('username', '')
#     channel_uid = request.args.get('channel_uid', '')
#     channel_doc = [
#         "uuid": channel_uid
#     ]
#     db.collection("users").document(user_uid).collection("subscriptions").insert(channel_doc)

@app.route("/user", methods=["GET"])
def getUserDetails():
    # uid = request.args.get('uid', '')
    uid = "4H3Cv1i8EVVUhKIHJc9Ek205nsr2"
    user_record = auth.get_user(uid)

    #TODO: Get user document from firestore too and add to resultant json

    user = {
        "uid": user_record.uid,
        "email": user_record.email,
        "display_name": user_record.display_name,
    }
    return json.dumps(user)

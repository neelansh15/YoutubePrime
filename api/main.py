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
    "databaseURL": "https://prime-43c05.firebaseio.com",
    "serviceAccount": "serviceAccountKey.json"
}


firebase = pyrebase.initialize_app(pyrebaseConfig)
pyreauth = firebase.auth()

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
    user = {
        "email": user_json['email'],
        "password": user_json['password'],
        "display_name": user_json['display_name'],
        "photo_url": user_json['photo_url'],
    }

    new_user = pyreauth.create_user_with_email_and_password(user["email"], user["password"])

    print(user["password"])
    
    db.collection("users").document(new_user["localId"]).set({
        "uid": new_user["localId"],
        "email": user["email"],
        "display_name": user["display_name"],
        "photo_url": user["photo_url"],
        "subscriber_count": 0
    })
    print(new_user)
    print('Sucessfully created new user: {0} {1}'.format(user["email"], new_user["localId"]))
    
    return new_user['idToken']

@app.route("/login", methods=["POST"])
def login():
    data = request.get_json(force=True)
    email = data["email"]
    password = data["password"]
    
    #TODO: Regex to check password like OSTPL Exp 2 here

    user = pyreauth.sign_in_with_email_and_password(email, password)
    if(user['idToken']):
        return user['idToken']
    else:
        return "[Error] " + user

@app.route("/upload-video", methods=['GET'])
def uploadVideo():
    file = request.form["file"]
    print(file)    
    # data = request.get_json(force=True)
    # token = data["idToken"]
    # decoded_token = auth.verify_id_token(token)
    # user_uid = decoded_token['uid']


    # bucket = storage.bucket()
    # blob = bucket.blob("videos/cIVZdgPl5deSZNwAnePk.mp4")

    # blob.upload_from_filename("C:\\Users\\vedant\\Desktop\\somaiya\\test.mp4")
    # return 'Successful'

@app.route("/download-video", methods=['GET'])
def downloadVideo():
    # data = request.get_json()
    # videoId = data['videoId']
    bucket = storage.bucket()
    blob = bucket.blob("videos/new.mp4")
    
    expiration_time = datetime.now(tz=gettz('Asia/Kolkata')) + timedelta(minutes=1)
    print(expiration_time)

    url = blob.generate_signed_url(expiration=expiration_time, version='v4')
    
    return f"<video src='{url}' width=500 height=500 autoplay></video><input value={url} disabled />"

@app.route("/subscribe", methods=['POST'])
def subscribe():
    data = request.get_json()
    token = data['idToken']
    decoded_token = auth.verify_id_token(token)
    user_uid = decoded_token['uid']
    print(user_uid)
    
    channel_uid = data['channel_uid']
    channel_doc = {
        "uuid": channel_uid
    }
    # when user subscribe add to list
    current_user = db.collection("users").document(channel_uid).get().to_dict()
    
    db.collection("users").document(channel_uid).update({
        "subscriber_count": int(current_user["subscriber_count"])+1
    })
    db.collection("users").document(user_uid).collection("subscriptions").add(channel_doc)

@app.route("/user", methods=["POST"])
def getUserDetails():

    #TODO: Auth token for security, or add firebase rule to accept an auth header

    reqJSON = request.get_json(force=True)
    uid = reqJSON["uid"]
    # user_record = auth.get_user(uid) NOT REQUIRED

    userDoc = db.collection("users").document(uid).get()
    userDocData = userDoc.to_dict()

    #TODO: ALso fetch and return videos
    return json.dumps(userDocData)



# NOT TESTED
@app.route("/user-subscription", methods=["POST"])
def getUserSubscribedChannels():
    data = request.get_json()
    token = data['idToken']
    decoded_token = auth.verify_id_token(token)
    user_uid = decoded_token['uid']
    
    channels = db.collection("users").document(user_uid).collection("subscriptions").stream()
    channel_uids = []
    video_ids = []
    
    for channel in channels:
        channel_uids.append(channel.id)
    
    for channel_uid in channel_uids:
        videos = db.collection("users").document(channel_uid).collection("videos").stream()
        for video in videos:
            video_ids.append(video.id)

    return video_ids


@app.route("/top-channels", methods=["POST"])
def getTopChannel():
    data = request.get_json()
    token = data['idToken']
    decoded_token = auth.verify_id_token(token)
    user_uid = decoded_token['uid']
    channels = db.collection(u'users').order_by(u'subscriber_count', direction=firestore.Query.DESCENDING).limit(3).stream()
    channel_ids = []
    for channel in channels:
        channel_ids.append(channel.id)
    
    channels = db.collection("users").document(user_uid).collection("subscriptions").stream()
    channel_uids = []
    for channel in channels:
        channel_uids.append(channel.id)
    for i in channel_ids:
        if i in channel_uids:
            channel_ids.remove(i)
        print(i)
        print("\n")
    return channel_ids


### FILEDS
'''
users
    login cred
    subscriber_count
    + subscriptions collection: list of subscribed channels
    + video collection: object of meta data for videos

videos:
    Meta data

Storage:
    Filename = video.id

#TODO
authentication in download video
use auth tokens instead of username in user subscriptions

Remove channels from top channels if user is already subscribed
get video data route for meta data in dashboard

REMOVE USER GOES SECOND FROM MIN MAX TIC TAC

upload video
single video route

'''

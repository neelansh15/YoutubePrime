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
    blob = bucket.blob("videos/cIVZdgPl5deSZNwAnePk.mp4")

    blob.upload_from_filename("C:\\Users\\vedant\\Desktop\\somaiya\\test.mp4")
    return 'Successful'

@app.route("/download-video", methods=['GET'])
def downloadVideo():
    bucket = storage.bucket()
    blob = bucket.blob("videos/new.mp4")
    
    expiration_time = datetime.now(tz=gettz('Asia/Kolkata'))+ timedelta(minutes=1)
    print(expiration_time)

    url = blob.generate_signed_url(expiration=expiration_time, version='v4')
    
    return f"<video src='{url}' width=500 height=500 autoplay></video><input value={url} disabled />"

@app.route("/subscribe", methods=['POST'])
def subscribe():
    data = request.get_json()
    # token = request.args.get('accessToken', '')
    # decoded_token = auth.verify_id_token(token)
    # user_uid = decoded_token['uid']
    user_uid = data['username']
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


# NOT TESTED
@app.route("/user-subscription", methods=["POST"])
def getUserSubscribedChannels():
    data = request.get_json()
    # token = request.args.get('accessToken', '')
    # decoded_token = auth.verify_id_token(token)
    # user_uid = decoded_token['uid']
    user_uid = data['username']
    print(user_uid)
    
    channels = db.collection("users").document(user_uid).collection("subscriptions").stream()
    channel_uids = []
    video_ids = []
    
    for channel in channels:
        channel_uids.append(channel.to_dict()["uuid"])
    
    for channel_uid in channel_uids:
        videos = db.collection("users").document(channel_uid).collection("videos").stream()
        for video in videos:
            video_ids.append(video.id)
    print(video_ids)
    return video_ids


@app.route("/top-channels", methods=["POST"])
def getTopChannel():
    channels = db.collection(u'users').order_by(u'subscriber_count', direction=firestore.Query.DESCENDING).limit(3).stream()
    for channel in channels:
        print(channel.id)


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
'''
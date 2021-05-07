import os
import json
from datetime import datetime, timedelta
from dateutil.tz import gettz

from flask import Flask, request, Response
from flask_cors import CORS, cross_origin
from firebase_admin import credentials, auth, storage, firestore, initialize_app


import pyrebase
app = Flask(__name__)
app.config['CORS_HEADERS'] = 'Content-Type'

CORS(app, resources={r"/login": {"origins": "http://localhost:8080"}})

@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    response.headers.add('Access-Control-Allow-Credentials', 'true')
    return response

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
initialize_app(cred, {
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
    
    return Response(new_user['idToken'], status=201, mimetype='application/json')

@app.route("/login", methods=["POST"])
# @cross_origin()
def login():
    data = request.get_json(force=True)
    email = data["email"]
    password = data["password"]
    
    #TODO: Regex to check password like OSTPL Exp 2 here

    user = pyreauth.sign_in_with_email_and_password(email, password)
    if (user['idToken']):
        return Response(user['idToken'], status=201, mimetype='application/json')

    else:
        return Response(user, status=404, mimetype='application/json')

@app.route("/upload", methods=['POST'])
def uploadVideo():
    if 'myfile' not in request.files:
        return "No file part"

    file = request.files["myfile"]
    file_extension = os.path.splitext(file.filename)[1]
    print(file.filename)
    print(file_extension)

    thumbnail = request.files["thumbnail"]
    thumbnail_extension = os.path.splitext(thumbnail.filename)[1]
    print(thumbnail.filename)
    
    
    data = request.form
    token = data["idToken"]
    decoded_token = auth.verify_id_token(token)
    user_uid = decoded_token['uid']

    doc = dict(request.form)
    doc.pop("idToken") #Don't need to return this from the form
    doc["type"] = file_extension
    doc["thumbnail_type"] = thumbnail_extension

    created_doc_tuple = db.collection("users").document(user_uid).collection("videos").add(doc)
    print("Returned Doc: ")
    print(created_doc_tuple)

    created_doc_ref = created_doc_tuple[1]

    video_id = created_doc_ref.id
    print(video_id)
    bucket = storage.bucket()

    blob_thumbnail = bucket.blob(f"images/{video_id}{thumbnail_extension}")
    blob_thumbnail.upload_from_string(thumbnail.read())
    blob_thumbnail.make_public()

    print("THUMBNAIL PUBLIC URL: ")
    print(blob_thumbnail.public_url)

    created_doc_ref.update({
        "uid": video_id,
        "thumbnail_url": blob_thumbnail.public_url
    })

    #Upload to gcloud bucket
    # bucket = storage.bucket()
    blob = bucket.blob(f"videos/{video_id}{file_extension}")
    blob.upload_from_string(file.read())


    return 'Successful ' + video_id

@app.route("/getVideo", methods=['POST'])
def getVideo():
    '''
    :Params: idToken, video_id, channel_id
    '''

    # TODO: AUTHENTICATION to see if user can access this video i.e. user is subscribed to this channel
    data = request.get_json()

    token = data['idToken']
    decoded_token = auth.verify_id_token(token)
    user_uid = decoded_token['uid']
    
    channel_uid = data['channel_id']
    print(user_uid)
    print(channel_uid)
    channels = db.collection("users").document(user_uid).collection("subscriptions").stream()
    
    channel_uids = []
    for channel in channels:
        channel_uids.append(channel.id)
    
    if channel_uid not in channel_uids:
        return "Unauthorized"
    #END Authentication

    video_id = data['video_id']
    meta = db.collection("users").document(channel_uid).collection("videos").document(video_id).get()
    meta = meta.to_dict()
    extension = meta["type"]

    bucket = storage.bucket()
    blob = bucket.blob(f"videos/{video_id}{extension}")    

    expiration_time = datetime.now(tz=gettz('Asia/Kolkata')) + timedelta(minutes=60)
    print(expiration_time)

    url = blob.generate_signed_url(expiration=expiration_time, version='v4')
    
    return json.dumps([url, meta])

@app.route("/subscribe", methods=['POST'])
def subscribe():
    data = request.get_json()
    token = data['idToken']
    decoded_token = auth.verify_id_token(token)
    user_uid = decoded_token['uid']
    print(user_uid)
    
    channel_uid = data['channel_id']
    channel_doc = {
        "uuid": channel_uid
    }
    # when user subscribe add to list
    current_user = db.collection("users").document(channel_uid).get().to_dict()
    
    db.collection("users").document(channel_uid).update({
        "subscriber_count": int(current_user["subscriber_count"])+1
    })
    db.collection("users").document(user_uid).collection("subscriptions").document(channel_uid).set(channel_doc)

    return Response("OK", status=201, mimetype='application/json')


@app.route("/user", methods=["POST"])
def getUserDetails():
    #TODO: Auth token for security, or add firebase rule to accept an auth header
    data = request.get_json()
    user_uid = data['user_id']
    # reqJSON = request.get_json(force=True)
    # uid = reqJSON["uid"]
    # user_record = auth.get_user(uid) NOT REQUIRED
    userDoc = db.collection("users").document(user_uid).get()
    userDocData = userDoc.to_dict()
    #TODO: ALso fetch and return videos
    return json.dumps(userDocData)

@app.route("/userWithToken", methods=["POST"])
def getUserDetailsUsingToken():
    #TODO: Auth token for security, or add firebase rule to accept an auth header
    data = request.get_json()
    token = data['idToken']
    decoded_token = auth.verify_id_token(token)
    user_uid = decoded_token['uid']
    # reqJSON = request.get_json(force=True)
    # uid = reqJSON["uid"]
    # user_record = auth.get_user(uid) NOT REQUIRED
    userDoc = db.collection("users").document(user_uid).get()
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
    print(token[:20])
    print(user_uid)

    
    channels = db.collection("users").document(user_uid).collection("subscriptions").stream()
    channel_uids = []
    video_ids = []
    
    for channel in channels:
        channel_uids.append(channel.id)
    
    print(channel_uids)
    for channel_uid in channel_uids:
        videos = db.collection("users").document(channel_uid).collection("videos").stream()
        for video in videos:
            video_ids.append((channel_uid, video.id))
    print(video_ids)

    return Response(json.dumps(video_ids), status=200, mimetype='application/json')


@app.route("/top-channels", methods=["POST"])
def getTopChannel():
    data = request.get_json()
    token = data['idToken']
    decoded_token = auth.verify_id_token(token)
    user_uid = decoded_token['uid']
    print(token[:20])

    print(user_uid)

    channels = db.collection(u'users').order_by(u'subscriber_count', direction=firestore.Query.DESCENDING).limit(10).stream()
    channel_ids = []
    for channel in channels:
        channel_ids.append(channel.id)
    
    channels = db.collection("users").document(user_uid).collection("subscriptions").stream()
    channel_uids = []
    for channel in channels:
        channel_uids.append(channel.id)
    for i in channel_ids:
        if i in channel_uids or i == user_uid:
            channel_ids.remove(i)
        print(i)
        print("\n")
    return Response(json.dumps(channel_ids), status=200, mimetype='application/json')

@app.route("/remove-subscription", methods=["POST"])
def removeSubscription():
    data = request.get_json()
    token = data['idToken']
    decoded_token = auth.verify_id_token(token)
    user_uid = decoded_token['uid']
    print(user_uid)
    
    channel_uid = data['channel_id']
    current_user = db.collection("users").document(channel_uid).get().to_dict()
    
    db.collection("users").document(channel_uid).update({
        "subscriber_count": int(current_user["subscriber_count"]) - 1
    })
    db.collection("users").document(user_uid).collection("subscriptions").document(channel_uid).delete()
    return Response("OK", status=200, mimetype='application/json')

@app.route("/video-meta", methods=["POST"])
def getMetaData():
    '''
    :Params: video_id and channel_id
    :returns: Meta data
    :return type: json
    '''
    data = request.get_json()
    video_id = data['video_id']
    channel_id = data['channel_id']
    meta = db.collection("users").document(channel_id).collection("videos").document(video_id).get()
    meta = meta.to_dict()
    meta['channel_id'] = channel_id

    return json.dumps(meta)


@app.route("/getAllSubsriptions", methods=["POST"])
def getSubscribedChannels():
    data = request.get_json()
    token = data['idToken']
    decoded_token = auth.verify_id_token(token)
    user_uid = decoded_token['uid']
    print(user_uid)
    channels = db.collection("users").document(user_uid).collection("subscriptions").stream()
    channel_uids = []
    
    for channel in channels:
        channel_uids.append(channel.id)
    return Response(json.dumps(channel_uids), status=200, mimetype='application/json')

@app.route("/getAllChannelVideos", methods=["POST"])
def getVideos():
    data = request.get_json()
    channel_id = data['channel_id']
    video_ids = []
    videos = db.collection("users").document(channel_id).collection("videos").stream()
    for video in videos:
        video_ids.append((channel_id, video.id))
    return Response(json.dumps(video_ids), status=200, mimetype='application/json')


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

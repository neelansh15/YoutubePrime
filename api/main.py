from datetime import datetime, timedelta
from dateutil.tz import gettz

from flask import Flask, request
app = Flask(__name__)

import firebase_admin
from firebase_admin import credentials, auth, storage
from flask import request

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    "storageBucket": "prime-43c05.appspot.com",
})

@app.route("/")
def hello():
    return "Hello world!"

@app.route("/register", methods=["POST"])
def register():
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

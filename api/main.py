from flask import Flask, request
app = Flask(__name__)

import firebase_admin
from firebase_admin import credentials, auth
from flask import request
from google.cloud import storage
import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="./serviceAccountKey.json"

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
        email='user@example.com',
        email_verified=False,
        phone_number='+15555550100',
        password='secretPassword',
        display_name='John Doe',
        photo_url='http://www.example.com/12345678/photo.png',
        disabled=False
    )
    print('Sucessfully created new user: {0}'.format(user.uid))

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



@app.route("/upload-video", methods=['GET','POST'])
def uploadVideo():
    if request.method == 'POST':
        storage_client = storage.Client()
        bucket = storage_client.bucket('prime-43c05.appspot.com')
        blob = bucket.blob("videos/new.mp4")

        blob.upload_from_filename("C:\\Users\\vedant\\Desktop\\somaiya\\test.mp4")
        return 'Successful'

@app.route("/download-video", methods=['GET','POST'])
def downloadVideo():
    if request.method == 'POST':
        storage_client = storage.Client()
        bucket = storage_client.bucket('prime-43c05.appspot.com')
        blob = bucket.blob("videos/new.mp4")

        blob.download_to_filename("C:\\Users\\vedant\\Desktop\\abc.mp4")
        return 'Successful'
# if given "videos/videoName" then storage.child("videos/videoName").get_url(None)


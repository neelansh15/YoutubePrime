<h1 align="center">Youtube Prime</h1>

[![](https://img.shields.io/badge/Made_with-Python-yellow?style=for-the-badge&logo=python)](https://python.org/) 
[![](https://img.shields.io/badge/Made_with-Flask-lightgrey?style=for-the-badge&logo=flask)](https://flask.palletsprojects.com/en/1.1.x/) 
[![](https://img.shields.io/badge/Made_with-Vue-brightgreen?style=for-the-badge&logo=vue.js)](https://vuejs.org/) 
[![](https://img.shields.io/badge/Made_with-Vuetify-blue?style=for-the-badge&logo=vuetify)](https://vuetifyjs.com/) 
<br /><br />
A new era of subscription-based Video sharing for content creators. Upload videos and share them with people subscribed to you. (Note: Payment is a future prospect, Subscribing is free as of now).

*Sem IV OSTPL Mini Project*

## Installation

### Prerequisite
You need to have a Google Firebase project, get the `serviceAccountKey.json` file (removed from this repo for security reasons), and put it in the `/api` directory. Next in `main.py` change the values of the `pyrebaseConfig` dictionary to match your firebase project.

### Backend (Python Flask)
cd into the `/api` directory. Before you run the flask server, you need to install all the python dependencies, run either `setapp` (Windows) or `export FLASK_APP=main.py` (Linux) and then run the flask server with `flask run`.

*Note: setapp.bat is just a command created to avoid typing the whole `set FLASK_APP=main.py` every time*

**Dependencies**
Flask
urllib3
firebase-admin
pyrebase4
dateutil
flask-cors
python-dateutil

**Steps:**
- `cd api`
- `setapp` or `export FLASK_APP=main.py`
- `flask run`

### Frontend
cd into the `/frontend` directory and run `yarn` to install all the dependencies. Use `yarn serve` to run the frontend server.
Steps:
- `cd api`
- `yarn`
- `yarn serve`

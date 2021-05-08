<div align="center">
  
  ![image](https://user-images.githubusercontent.com/53081208/117554459-7e350c00-b075-11eb-9791-9770e68b2be0.png)
  
</div>

<div align="center">
<br />
  
[![](https://img.shields.io/badge/Made_with-Python-yellow?style=for-the-badge&logo=python)](https://python.org/) 
[![](https://img.shields.io/badge/Made_with-Flask-lightgrey?style=for-the-badge&logo=flask)](https://flask.palletsprojects.com/en/1.1.x/) 
[![](https://img.shields.io/badge/Made_with-Vue-brightgreen?style=for-the-badge&logo=vue.js)](https://vuejs.org/) 
[![](https://img.shields.io/badge/Made_with-Vuetify-blue?style=for-the-badge&logo=vuetify)](https://vuetifyjs.com/) 

</div>
<br />
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

## Screenshots
![image](https://user-images.githubusercontent.com/53081208/117554544-f7346380-b075-11eb-9791-b2042d46ac0c.png)
![image](https://user-images.githubusercontent.com/53081208/117554557-159a5f00-b076-11eb-9e78-d4c3f8f83d35.png)
![image](https://user-images.githubusercontent.com/53081208/117554568-32369700-b076-11eb-9c7e-ecbcaa9faef7.png)
![image](https://user-images.githubusercontent.com/53081208/117554585-3f538600-b076-11eb-8ef8-c5964b9c057e.png)
![image](https://user-images.githubusercontent.com/53081208/117554609-6ad67080-b076-11eb-8069-6b7902819046.png)
![image](https://user-images.githubusercontent.com/53081208/117554625-8772a880-b076-11eb-99f3-471f70eb7270.png)
![image](https://user-images.githubusercontent.com/53081208/117554596-54c8b000-b076-11eb-8cf1-235b6b78a635.png)
![image](https://user-images.githubusercontent.com/53081208/117554704-e9cba900-b076-11eb-9002-de471becc891.png)
![image](https://user-images.githubusercontent.com/53081208/117554641-9b1e0f00-b076-11eb-9055-d5cfee9d9e87.png)

## Future Prospects
- Remaining functionality like ability to edit user info (Display name, Profile pic), edit video info(Title, description), etc.
- Payment gateway for subscribing to a user

from flask import Flask, request,Response

app = Flask(__name__)

@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    response.headers.add('Access-Control-Allow-Credentials', 'true')
    return response

@app.route("/hello", methods=["POST", "GET"])
def hello():
  # status_code = Response(status=202)
  return Response("{'a':'b'}", status=201, mimetype='application/json')

# @app.route("/login", methods=["POST"])
# # @cross_origin()
# def login():
#     print("HERE")
#     data = request.get_json(force=True)
#     email = data["email"]
#     password = data["password"]
    
#     #TODO: Regex to check password like OSTPL Exp 2 here

#     user = pyreauth.sign_in_with_email_and_password(email, password)
#     if(user['idToken']):
#         return user['idToken']
#     else:
#         return "[Error] " + user
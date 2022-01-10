
from flask import Flask
from google.cloud import storage
from google.oauth2 import service_account
from wsgiref import simple_server
import os
import ast
from flask import Flask, session, request, Response, jsonify
from dotenv import load_dotenv
load_dotenv()

key_value=os.getenv("Key_value")
# sample_json={"user":os.getenv("user"),"password":os.getenv("password"),"age":os.getenv("age"),"height":os.getenv("height")}
creds=os.getenv('creds')
creds1=ast.literal_eval(creds)
print(type(creds1))


app = Flask(__name__)



@app.route('/', methods=['GET', 'POST'])
def index():
    return "Flask app is running and this is the {0} overall dict, now the account type is {1}".format(creds1,creds1['type'])

port = int(os.getenv("PORT", 5001))

if __name__ == "__main__":
    host = '0.0.0.0'
    #app.run()
    httpd = simple_server.make_server(host=host, port=port, app=app)
    #httpd = simple_server.make_server(host='127.0.0.1', port=5000, app=app)
    # print("Serving on %s %d" % (host, port))
    httpd.serve_forever()

from flask import Flask
# from google.cloud import storage
# from google.oauth2 import service_account
from wsgiref import simple_server
import os
import ast
from flask import Flask, session, request, Response, jsonify
from dotenv import load_dotenv
load_dotenv()
import pandas as pd

# key_value=os.getenv("Key_value")
# sample_json={"user":os.getenv("user"),"password":os.getenv("password"),"age":os.getenv("age"),"height":os.getenv("height")}
# creds=os.getenv('creds')
# creds1=ast.literal_eval(creds)
# print(type(creds1))


app = Flask(__name__)



@app.route('/', methods=['GET', 'POST'])
def index():
    root = os.getcwd()
    print(os.getcwd())
    # test_dir = os.path.join(os.getcwd(),"Testing_directory")
    test_dir = os.path.join("Testing_directory")
    os.makedirs(test_dir, exist_ok=True)
    os.chdir(test_dir)
    # os.mkdir("Testing_directory")
    # os.chdir("Testing_directory")
    data = {'Name': ['Tom', 'Joseph', 'Krish', 'John','Ravi','Elias'], 'Age': [20, 21, 19, 18,28,31]}
    df = pd.DataFrame(data)
    outfile = open('Testing_df.csv', 'wb')
    df.to_csv('Testing_df.csv')
    df_new = pd.read_csv("Testing_df.csv")
    print(df_new)
    print(df.shape)
    shape = df_new.shape
    # os.close("Testing_df.csv")
    outfile.close()
    # os.rmdir(os.path.join(root,test_dir))
    return f"Flask app is running and shape = {shape}"
    # return f"Flask app is running successfully and below is the json for it {sample_json}"

port = int(os.getenv("PORT", 5001))

if __name__ == "__main__":
    host = '0.0.0.0'
    #app.run()
    httpd = simple_server.make_server(host=host, port=port, app=app)
    #httpd = simple_server.make_server(host='127.0.0.1', port=5000, app=app)
    # print("Serving on %s %d" % (host, port))
    httpd.serve_forever()
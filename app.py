from flask import Flask
import os
import pandas as pd
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    # root = os.getcwd()
    # print(os.getcwd())
    # test_dir = os.path.join(os.getcwd(),"Testing_directory")
    # os.makedirs(test_dir, exist_ok=True)
    # os.chdir(test_dir)
    # # os.mkdir("Testing_directory")
    # # os.chdir("Testing_directory")
    # data = {'Name': ['Tom', 'Joseph', 'Krish', 'John'], 'Age': [20, 21, 19, 18]}
    # df = pd.DataFrame(data)
    # df.to_csv("Testing_df.csv")
    # df_new = pd.read_csv("Testing_df.csv")
    # print(df_new)
    # print(df.shape)
    # shape = df_new.shape
    # os.rmdir(os.path.join(root,test_dir))
    # return f"Flask app is running and shape = {shape}"
    return "this is just a testing app"


if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000)

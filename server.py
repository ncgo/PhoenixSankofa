# app.py
from flask import Flask  # import flask

app = Flask(__name__)  # create an app instance

# ! might scrap this entirely


@app.route("/")  # at the end point /
def hello():  # call method hello
    return "ok"  # which returns "hello world"


if __name__ == "__main__":  # on running python app.py
    app.run()  # run the flask app


from flask import Flask
from send import send

app = Flask(__name__)

# http://localhost:8800/
@app.route("/", methods=['GET'])
def hello_world():
    # run other code
    return "Hello, world"

# http://localhost:8800/abc
@app.route("/abc", methods=['GET'])
def abc_view():
    # run other code
    return "Hello, world"

@app.route("/weather_notification", methods=['POST'])
def weather_notification():
    # run other code
    send()
    return "Done"
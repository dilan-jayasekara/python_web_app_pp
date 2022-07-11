from flask import Flask
app = Flask(__name__)


@app.route("/")
def home():
    return "Hello, this is a sample Python Web App running on Flask Framework! And I just did some modifications to the code and lets see how good DevOps is!"


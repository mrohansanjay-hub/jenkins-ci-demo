from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "FINAL RETEST – CI/CD PIPELINE VERIFIED"


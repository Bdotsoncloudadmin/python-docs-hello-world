from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World! Happy Tuesday!!! Thank you for watching my tutorial video!"

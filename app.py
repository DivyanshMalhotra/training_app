from flask import Flask
app = Flask(__name__)
@app.route("/")
def hello_world():
    return "<h2> This is the first web app by Divyansh Malhotra</h2>"
if __name__ == "__main__":
    app.run(host = "0.0.0.0")
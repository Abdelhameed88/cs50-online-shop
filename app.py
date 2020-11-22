from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("login.html")


@app.route("/login", methods=(["POST"]))
def login():
    name = request.args.get("username")
    password = request.args.get("password")
    return render_template("index.html")

@app.route("/login", methods=(["GET"]))
def loginPage():
    return render_template("login.html")


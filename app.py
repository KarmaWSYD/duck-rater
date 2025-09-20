from flask import Flask, render_template, request
import sqlite3
from werkzeug.security import generate_password_hash
import random
import db

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/create_account", methods=["POST"])
def create_account():
    username = request.form["username"]
    password1 = request.form["password1"]
    password2 = request.form["password2"]
    if password1 != password2:
        return "Error: Passwords do not match"
    password_hash = generate_password_hash(password1) # return string includes the method, salt and hash ($ as separator), the salt is unique for each instance

    try:
        sql = """INSERT INTO users (username, password_hash) VALUES (?, ?)"""
        db.execute(sql, [username, password_hash])
    except sqlite3.IntegrityError:
        suggest_username = username + f"{random.randint(1, 99)}"
        # TODO Add a check for if the suggested username already exists
        return f"Error: Username has already been taken, try a different username, for example: {suggest_username}"

    return "Created account"
from flask import Flask, render_template, redirect, request, session, abort
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash
import random
import db
import os
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("SECRET")

def require_login():
    if "username" not in session:
        abort(403) # We could also redirect to login page instead

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

    session["username"] = username
    return redirect("/")

@app.route("/login")
def login_get():
    return render_template("login.html")

@app.route("/login", methods=["POST"])
def login_post():
    username = request.form["username"]
    password = request.form["password"]
    sql = """
        SELECT password_hash 
        FROM users
        WHERE username = ?
        ;"""
    password_hash = db.query_one(sql, [username])
    if not password_hash:
        return "ERROR: Could not find user"
    else:
        password_hash = password_hash[0]

    if check_password_hash(password_hash, password):
        session["username"] = username
        return redirect("/")
    else:
        return "Incorrect password"
    
@app.route("/logout")
def logout():
    del session["username"]
    return redirect("/")

@app.route("/new-duck")
def new_duck_get():
    require_login()
    return render_template("add_item.html")

@app.route("/new-duck", methods=["POST"])
def new_duck_post():
    require_login()
    duck_name = request.form("duck_name")
    duck_image = request.form("duck_image")
    duck_description = request.form("duck_description")
    duck_description = "No description provided"
    
    sql = """
    INSER INTO ducks (duck_name, duck_image, duck_description) 
    VALUES (?, ?, ?)
    ;"""
    db.execute(sql, [duck_name, duck_image, duck_description])


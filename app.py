from flask import Flask, render_template, redirect, request, session, abort, flash
from werkzeug.security import generate_password_hash, check_password_hash
from secrets import token_hex
import random
import os
import items, users
from dotenv import load_dotenv 
# uses locally defined dotenv.py, but should be compatible with python-dotenv
# we're not using the proper module due to course requirements
load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("SECRET")

def require_login():
    if "username" not in session:
        abort(403) # We could also redirect to login page instead

def check_csrf():
    if "csrf_token" not in request.form:
        abort(403)
    if request.form["csrf_token"] != session["csrf_token"]:
        abort(403)

@app.route("/")
def index():
    all_items = items.get_ducks()
    return render_template("index.html", items=all_items)

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/create_account", methods=["POST"])
def create_account():
    username = request.form["username"]
    password1 = request.form["password1"]
    password2 = request.form["password2"]
    if password1 != password2:
        flash("Error: Passwords do not match")
        return redirect("/register")
    password_hash = generate_password_hash(password1)

    if not users.create_user(username, password_hash):
        suggest_username = username + f"{random.randint(1, 9999)}" # This could have duplicates
        flash(f"Error: Username has already been taken, try a different username, for example: {suggest_username}")
        return redirect("/register")

    session["username"] = username
    return redirect("/")

@app.route("/login", methods=["GET"])
def login_get():
    return render_template("login.html")

@app.route("/login", methods=["POST"])
def login_post():
    username = request.form["username"]
    password = request.form["password"]
    user_id, password_hash = users.login(username)
    if not password_hash:
        flash("ERROR: Could not find user, are you sure you have an account?")
        return redirect("/login")

    if check_password_hash(password_hash, password):
        session["username"] = username
        session["csrf_token"] = token_hex(16)
        session["user_id"] = user_id
        return redirect("/")
    else:
        flash("Incorrect password")
        return redirect("/login")
    
@app.route("/logout")
def logout():
    del session["username"]
    return redirect("/")

@app.route("/new-duck", methods=["GET"])
def new_duck_get():
    require_login()
    categories = items.get_categories()
    return render_template("add_item.html", categories=categories)

@app.route("/new-duck", methods=["POST"])
def new_duck_post():
    require_login()
    check_csrf()
    duck_name = request.form["duck-name"]
    if not duck_name:
        duck_name = "Untitled Duck"
    duck_description = request.form["duck-description"]
    if not duck_description:
        duck_description = "No description provided"
    duck_category = request.form["category"]
    
    item_id = items.create_duck(creator=session["user_id"], name=duck_name, description=duck_description, category=duck_category)
    
    file = request.files["duck-image"]
    duck_image = file.read()
    
    items.create_image(duck_image, item_id)
    # should we support multiple images being made on creation?
    return redirect("/item/" + str(item_id))

@app.route("/duck-images/<int:item_id>", methods=["GET"])
def get_image(item_id):
    return items.get_image(item_id)

@app.route("/item/<int:item_id>", methods=["GET"])
def show_item(item_id):
    item = items.get_duck(item_id)
    images = items.get_images(item_id)
    category = items.get_category(item["category"])
    return render_template("show_item.html", images=images, item=item, category=category)

@app.route("/remove-item/<int:item_id>", methods=["GET", "POST"])
def remove_item(item_id):
    require_login()

    item = items.get_duck(item_id)
    if not item:
        abort(404)
    if item["user_id"] != session["user_id"]:
        abort(403)

    if request.method == "GET":
        return render_template("remove_item.html", item=item)

    if request.method == "POST":
        check_csrf()
        if "remove" in request.form:
            items.remove_duck(item_id)
            return redirect("/")
        else:
            return redirect("/item/" + str(item_id))

@app.route("/edit-item/<int:item_id>", methods=["GET"])
def edit_item(item_id):
    require_login()
    item = items.get_ducks(item_id)
    if not item:
        abort(404)
    if item["user_id"] != session["user_id"]:
        abort(403)

    return render_template("edit_item.html", item=item, categories=items.get_categories())
        
@app.route("/update-item/<int:item_id>", methods=["POST"])
def update_item():
    require_login()
    check_csrf()

    item_id = request.form["item_id"]
    item = items.get_duck(item_id)
    if not item:
        abort(404)
    if item["user_id"] != session["user_id"]:
        abort(403)

    title = request.form["title"]
    if not title or len(title) > 50:
        abort(403)
    description = request.form["description"]
    if not description or len(description) > 1000:
        abort(403)

    items.update_duck(item_id, title, description)

    return redirect("/item/" + str(item_id))

    
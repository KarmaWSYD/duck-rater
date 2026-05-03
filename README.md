# duck-rater

## Application Features

### Implemented Features:

* The user can create an account and login to the application.
* The user can add a title, description and an image for the duck
* The user can choose a category the duck (e.g. real duck, drawing of a duck, rubber duck)
* The user can see images of ducks posted to the application.
* The user can modify and delete posts about ducks. 
* The user can rate ducks on a scale of 1-5
* Users can add and delete comments about ducks under posts
* The user can search posts with a keyword.
* The application has an user page that shows statistics and any posts created by the user.

### Planned Features:

### Known Issues:

## How to install:
Tested on Python 3.13.8, other versions may or may not work.

Start by cloning the repository:
```
$ git clone https://github.com/KarmaWSYD/duck-rater.git
```

### Option 1: Manual install
In a Python virtual environment (venv)

### 1.1 Install the `flask`-library:
Tested on Flask version 3.1.2, other versions may or may not work.
```
$ pip install flask==3.1.2
```

### 1.2 Create the database:

```
$ sqlite3 database.db < schema.sql
$ sqlite3 database.db < init.sql
```
### Option 2: Setup script
This option is not guaranteed to work but is provided for the sake of convenience. Please use Option 1 if there are any issues.
```
$ ./setup.sh
```

## Start the application:
Using a Flask development server (as is done here) is not suitable for production use.

First activate the venv, then run the following command:
```
$ flask run
```

## Environment variables:
The application stores a secret key in a .env file in the directory it's installed in.
This file, and the secret in it (formatted as `SECRET=INSERT_SECRET_HERE`, with "INSERT_SECRET_HERE" being replaced with a random string of characters) are automatically created during the installation process.
If this process fails or you'd like to create this file yourself, you can do so by running 

```
$ cp example.env .env
```

and then using your favourite text editor to edit the value of the `SECRET=` key to a suitable value. This value should be complex and random to ensure security.
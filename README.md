# duck-rater


## Application Features

### Implemented Features:

* The user can create an account and login to the application.
* The user can add (pictures and/or text) about ducks (title, image, description)

### Planned Features:

* The user can modify and delete posts (pictures or text) about ducks. 
* The user can choose one or more categories for the duck (e.g. real duck, drawing of a duck, rubber duck)
* The user can see ducks posted to the application.
* The user can search posts with a keyword.
* The application has an user page that shows statistics and any posts created by the user.
* The user can rate ducks on a scale of 1-5 as well as add written reviews of ducks.

### Known Issues:
* Information about ducks is not shown properly in the index
* New Duck option gives an error instead of redirecting to a login/register page


## How to install:
In a Python virtual environment (venv)
Tested on Python 3.13.8, other versions may or may not work.
### Install the `flask`-library:
Tested on Flask version 3.1.2, other versions may or may not work.
```
$ pip install flask==3.1.2
```

### Create the database:

```
$ sqlite3 database.db < schema.sql
```
### Start the application:

Using a Flask development server (as is done here) is not suitable for production use.

```
$ flask run
```
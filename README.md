# duck-rater

## Application Features

### Implemented Features:

* The user can create an account and login to the application.
* The user can add a title, description and an image for the duck
* The user can choose a category the duck (e.g. real duck, drawing of a duck, rubber duck)
* The user can see images of ducks posted to the application.
* The user can modify and delete posts about ducks. 
* The user can rate ducks on a scale of 1-5
* The user can search posts with a keyword.
* The application has an user page that shows statistics and any posts created by the user.


### Planned Features:
* Forum features
* More statistics for the user page
* UI improvements

### Known Issues:
* Issue in the SQL Schema causing a crash

## How to install:
Tested on Python 3.13.8, other versions may or may not work.

Start by cloning the repository:
```
$ git clone https://github.com/KarmaWSYD/duck-rater.git
```

### Option 1: Setup script
This option may not work on all platforms, if it doesn't, please follow the manual install instructions instead.
```
$ ./setup.sh
```

### Option 2: Manual install
In a Python virtual environment (venv)

### 2.1 Install the `flask`-library:
Tested on Flask version 3.1.2, other versions may or may not work.
```
$ pip install flask==3.1.2
```

### 2.2 Create the database:

```
$ sqlite3 database.db < schema.sql
$ sqlite3 database.db < init.sql
```
## Start the application:
Using a Flask development server (as is done here) is not suitable for production use.

```
$ flask run
```

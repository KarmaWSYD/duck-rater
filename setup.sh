#!/usr/bin/bash

python_setup=`python3 -m venv venv && source venv/bin/activate`
echo $python_setup
install_dependencies=`pip install flask==3.1.2`
echo $install_dependencies
sqlite_setup=`sqlite3 database.db < schema.sql`
echo $sqlite_setup
sqlite_init=`sqlite3 database.db < init.sql`
echo $sqlite_init
echo "Setup complete, you can run the app by using flask run"

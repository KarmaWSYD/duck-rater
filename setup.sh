#!/usr/bin/bash
echo "Setting up the venv and installing dependencies"
python_setup=`python3 -m venv venv && source venv/bin/activate && pip install flask==3.1.2`
echo "Setting up the database"
sqlite_setup=`sqlite3 database.db < schema.sql && sqlite3 database.db < init.sql`
echo "Setup complete, you can run the app by running the following command:"
echo "source venv/bin/activate && flask run"
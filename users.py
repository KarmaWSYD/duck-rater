import db
import sqlite3

def create_user(username, password_hash):
    sql = """INSERT INTO users (username, password_hash) VALUES (?, ?)"""
    try:
        db.execute(sql, [username, password_hash])
        return True
    except sqlite3.IntegrityError:
        return False
    
def login(username):
    sql = """
        SELECT password_hash 
        FROM users
        WHERE username = ?
        ;"""
    password_hash = db.query_one(sql, [username])
    if not password_hash:
        return False
    else:
        password_hash = password_hash[0]
        return password_hash
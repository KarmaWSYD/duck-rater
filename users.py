import db
import sqlite3
from typing import Union, Optional

def create_user(username, password_hash) -> bool:
    sql = """INSERT INTO users (username, password_hash) VALUES (?, ?)"""
    try:
        db.execute(sql, [username, password_hash])
        return True
    except sqlite3.IntegrityError:
        return False
    
def login(username) -> tuple:
    sql = """
        SELECT id, password_hash 
        FROM users
        WHERE username = ?
        ;"""
    user_id, password_hash = db.query_one(sql, [username]) or (None, None)
    return (user_id, password_hash)
    
def get_user(id):
    sql = """
    SELECT id, username 
    FROM users 
    WHERE id = ?
    ;"""
    return db.query_one(sql, [id])

def get_ducks(user) -> Optional[list]:
    sql = """
        SELECT id, creator, duck_name AS title, duck_description AS description 
        FROM ducks
        WHERE creator = ?
        ORDER BY id DESC
        ;"""
    return db.query_all(sql, [user])
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
    
def login(username) -> Union[list, bool]:
    sql = """
        SELECT id, password_hash 
        FROM users
        WHERE username = ?
        ;"""
    result = db.query_one(sql, [username])
    if not result:
        return False
    else:        
        return result
    
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
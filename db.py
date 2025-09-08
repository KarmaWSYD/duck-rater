# Database code
import sqlite3
from flask import g

def _get_connection():
    conn = sqlite3.connect("database.db")
    conn.execute("PRAGMA foreign_keys ON")
    conn.row_factory = sqlite3.Row
    
    return conn

def execute(sql, params=[]):
    conn = _get_connection()
    result = conn.execute(sql, params)
    conn.commit()
    g.last_insert_id = result.lastrowid
    conn.close()

# is this actually necessary?
def last_insert_id():
    return g.last_insert_id

def query_all(sql, params=[]):
    conn = _get_connection()
    result = conn.execute(sql, params).fetchall()
    conn.close()
    return result

def query_all(sql, params=[]):
    conn = _get_connection()
    result = conn.execute(sql, params).fetchone()
    conn.close()
    return result
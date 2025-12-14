import db
import sqlite3

def create_duck(creator, name, description, category):
    sql = """
        INSERT INTO ducks (creator, duck_name, duck_description, category) 
        VALUES (?, ?, ?, ?)
        ;"""
    db.execute(sql, [creator, name, description, category])
    return db.last_insert_id() 

def get_duck(id):
    sql = """
    SELECT id, creator, duck_name AS title, duck_description AS description, category
    FROM ducks
    WHERE ducks.id = ?
    ;"""
    return db.query_one(sql, [id])

def get_ducks():  
    sql = """
        SELECT id, creator, duck_name AS title, duck_description AS description 
        FROM ducks
        ORDER BY id DESC
        ;"""
    return db.query_all(sql)

def find_items(query):
    sql = """SELECT id, duck_name AS title
             FROM ducks
             WHERE duck_name LIKE ? OR duck_description LIKE ?
             ORDER BY id DESC"""
    like = "%" + query + "%"
    return db.query_all(sql, [like, like])

def remove_duck(id):
    sql = """
    DELETE FROM images WHERE parent_id = ?
    ;"""
    db.execute(sql, [id])
    sql = """
    DELETE FROM comments WHERE parent_id = ?
    ;"""
    db.execute(sql, [id])
    sql = """
    DELETE FROM ducks WHERE id = ?
    ;"""
    db.execute(sql, [id])

def update_duck(id, title, description):
    sql = """
    UPDATE ducks 
    SET title = ?,
        description = ?
    WHERE id = ?
    ;"""
    db.execute(sql, [id, title, description])

def create_image(image, parent_id):
    sql = """
    INSERT INTO images (parent_id, duck_image) VALUES (?, ?)
    ;"""
    db.execute(sql, [parent_id, image])

def get_image(id):
    sql = f"""
    SELECT duck_image
    FROM images
    WHERE id = ?
    ;"""
    result = db.query_one(sql, [id])
    return result[0] if result else None

def get_images(id):
    sql = f"""
    SELECT id FROM images WHERE parent_id = ?
    ;"""
    return db.query_all(sql, [id])

def get_categories():
    sql = """
    SELECT id, name, description
    FROM categories
    ;"""
    return db.query_all(sql)

def get_category(id):
    sql = """
    SELECT name, description
    FROM categories
    WHERE id = ?
    ;"""
    return db.query_one(sql, [id])

def get_rating(id, user):
    sql = """
    SELECT rating FROM ratings
    WHERE parent_id = ?
        AND user_id = ? 
    ;"""
    result = db.query_one(sql, [id, user])
    return result[0] if result else None

def get_ratings_count(id):
    sql = """
    SELECT COUNT(rating) FROM ratings
    WHERE parent_id = ?
    ;"""
    return db.query_one(sql, [id])

def get_average_rating(id):
    sql = """
    SELECT AVG(rating) FROM ratings
    WHERE parent_id = ?
    ;"""
    return db.query_one(sql, [id])

def add_rating(id, user, rating):
    sql = """
    INSERT INTO ratings (parent_id, user_id, rating)
    VALUES (?, ?, ?)
    ON CONFLICT(user_id)
    DO
        UPDATE SET rating = ?
        WHERE parent_id = ?
            AND user_id = ?
    ;"""
    db.execute(sql, [id, user, rating, rating, id, user])

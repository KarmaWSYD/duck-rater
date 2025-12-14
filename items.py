import db

def create_duck(name, description):
    sql = """
        INSERT INTO ducks (duck_name, duck_description) 
        VALUES (?, ?)
        ;"""
    db.execute(sql, [name, description])
    return db.last_insert_id() 

def get_duck(id):
    sql = """
    SELECT ducks.id AS id, ducks.duck_name AS title, ducks.duck_description AS description 
    FROM ducks
    WHERE ducks.id = ?
    ;"""
    return db.query_one(sql, [id])

def get_all_ducks():  
    sql = """
        SELECT ducks.duck_name AS title, ducks.duck_description AS description 
        FROM ducks
        ORDER BY ducks.id DESC
        ;"""
    return db.query_all(sql)

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


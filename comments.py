import db

def get_comments(item_id):
    return db.query_all("""
                        SELECT comments.id, comments.user_id, comments.comment AS comment_text, users.username AS user
                        FROM comments
                        LEFT JOIN users
                          ON users.id = comments.user_id
                        WHERE comments.parent_id = ?
                        ORDER BY comments.id ASC
                        ;""",
                        [item_id]
    )
    
def add_comment(item_id, user_id, comment) -> None:
    db.execute("""
               INSERT INTO comments
               parent_id, user_id, comment
               VALUES
               (?, ?, ?)
               ;""",
               [item_id, user_id, comment])

def edit_comment(item_id, comment_id, comment) -> None:
    db.execute("""
               UPDATE comments
               SET comment = ?
               WHERE parent_id = ?
                 AND comment_id = ? 
               ;"""
               )
        
def delete_comment(item_id, comment_id, user_id) -> None:
    db.execute("""
               DELETE FROM comments
               WHERE parent_id = ?
                 AND comment_id = ?
                 AND user_id = ?
               ;""",
               [item_id, comment_id, user_id])
CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    username TEXT UNIQUE,
    password_hash TEXT
);

CREATE TABLE categories (
    id INTEGER PRIMARY KEY,
    name TEXT,
    description TEXT
);

CREATE TABLE ducks (
    id INTEGER PRIMARY KEY,
    creator INTEGER,
    CONSTRAINT fk_creator
      FOREIGN KEY (creator) 
      REFERENCES users(id)
      ON DELETE CASCADE,
    duck_name TEXT,
    duck_description TEXT,
    category INTEGER,
    CONSTRAINT fk_ducks
      FOREIGN KEY (parent_id) 
      REFERENCES ducks(id)
      ON DELETE CASCADE,
);

CREATE TABLE ratings (
    id INTEGER PRIMARY KEY,
    parent_id INTEGER,
    CONSTRAINT fk_ducks
      FOREIGN KEY (parent_id) 
      REFERENCES ducks(id)
      ON DELETE CASCADE,
    user_id INTEGER,
    CONSTRAINT fk_user
      FOREIGN KEY (user_id) 
      REFERENCES users(id)
      ON DELETE CASCADE,
    rating INTEGER,
    UNIQUE (parent_id,user_id)
    
);

CREATE TABLE comments (
    id INTEGER PRIMARY KEY,
    parent_id INTEGER,
    CONSTRAINT fk_ducks
      FOREIGN KEY (parent_id) 
      REFERENCES ducks(id)
      ON DELETE CASCADE,
    user_id INTEGER REFERENCES users
    comment TEXT
);

CREATE TABLE images (
    id INTEGER PRIMARY KEY,
    parent_id INTEGER,
    CONSTRAINT fk_ducks
      FOREIGN KEY (parent_id) 
      REFERENCES ducks(id)
      ON DELETE CASCADE,
    duck_image BLOB
);


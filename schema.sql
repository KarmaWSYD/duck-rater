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
    creator INTEGER REFERENCES users(id) ON DELETE CASCADE,
    duck_name TEXT,
    duck_description TEXT,
    category INTEGER REFERENCES categories(id) ON DELETE CASCADE
);

CREATE TABLE ratings (
    id INTEGER PRIMARY KEY,
    parent_id INTEGER REFERENCES ducks(id) ON DELETE CASCADE,
    user_id INTEGER REFERENCES users(id) ON DELETE CASCADE,
    rating INTEGER,
    UNIQUE (parent_id,user_id)
);

CREATE TABLE comments (
    id INTEGER PRIMARY KEY,
    parent_id INTEGER,
    parent_id INTEGER REFERENCES ducks(id) ON DELETE CASCADE,
    user_id INTEGER REFERENCES users(id) ON DELETE CASCADE,
    comment TEXT
);

CREATE TABLE images (
    id INTEGER PRIMARY KEY,
    parent_id INTEGER REFERENCES ducks(id) ON DELETE CASCADE,
    duck_image BLOB
);
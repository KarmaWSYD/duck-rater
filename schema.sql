CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    username TEXT UNIQUE,
    password_hash TEXT
);

CREATE TABLE ducks (
    id INTEGER PRIMARY KEY,
    duck_name TEXT,
    duck_description TEXT
    category INTEGER REFERENCES categories
);

CREATE TABLE comments (
    id INTEGER PRIMARY KEY,
    parent_id INTEGER REFERENCES ducks, -- do we not need to specify this as ducks.id?
    comment TEXT
);

CREATE TABLE images (
    id INTEGER PRIMARY KEY,
    parent_id INTEGER REFERENCES ducks,
    duck_image BLOB
);

CREATE TABLE categories (
    id INTEGER PRIMARY KEY,
    name TEXT,
    description TEXT
);
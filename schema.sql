CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    username TEXT UNIQUE,
    password_hash TEXT
);

CREATE TABLE ducks (
    id INTEGER PRIMARY KEY,
    duck_name TEXT,
    duck_image BLOB,
    duck_description TEXT
);


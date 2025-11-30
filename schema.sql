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

CREATE TABLE comments (
id INTEGER PRIMARY KEY,
parent_id INTEGER REFERENCES ducks, -- do we not need to specify this as ducks.id?
comment TEXT
);

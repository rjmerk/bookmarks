CREATE TABLE bookmarks
(
    id      SERIAL PRIMARY KEY,
    url     TEXT UNIQUE NOT NULL,
    name    TEXT        NOT NULL,
    created TIMESTAMP   NOT NULL
);

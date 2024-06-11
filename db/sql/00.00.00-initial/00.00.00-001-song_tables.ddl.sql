CREATE TABLE song (
    id          VARCHAR(50) NOT NULL PRIMARY KEY,
    author      VARCHAR(100) NOT NULL,
    title       VARCHAR(100) NOT NULL
);

CREATE TABLE song_country (
    song_id     VARCHAR(50) NOT NULL REFERENCES song(id),
    country     VARCHAR(100) NOT NULL
);

CREATE TABLE song_lyrics (
    song_id     VARCHAR(50) NOT NULL PRIMARY KEY REFERENCES song(id),
    lyrics      TEXT NOT NULL
);

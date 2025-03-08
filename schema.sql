CREATE TABLE IF NOT EXISTS posts (
    post_id SERIAL PRIMARY KEY,
    data_coleta TIMESTAMPTZ NOT NULL,
    url_post TEXT UNIQUE NOT NULL,
    data_post TIMESTAMPTZ NOT NULL,
    usuario TEXT,
    titulo TEXT NOT NULL,
    reacoes_post INTEGER,
    conteudo_post TEXT
);

CREATE TABLE IF NOT EXISTS comments (
    comment_id SERIAL PRIMARY KEY,
    post_id INTEGER REFERENCES posts(post_id) ON DELETE CASCADE,
    autor TEXT,
    data TIMESTAMPTZ,
    conteudo TEXT,
    reacoes INTEGER
);
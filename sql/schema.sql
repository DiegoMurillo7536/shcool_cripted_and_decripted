CREATE TABLE IF NOT EXISTS notes (
    id SERIAL PRIMARY KEY,
    nota BYTEA,
    comentario BYTEA,
    id_profesor INTEGER,
    id_alumno INTEGER
);
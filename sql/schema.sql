CREATE TABLE IF NOT EXISTS notes (
    id SERIAL PRIMARY KEY,
    nota BYTEA,
    comentario BYTEA,
    id_profesor INTEGER,
    id_alumno INTEGER
);

CREATE TABLE teachers (
    id SERIAL PRIMARY KEY,
    document_number BYTEA NOT NULL,
    full_name BYTEA NOT NULL,
    email BYTEA NOT NULL,
    age INTEGER NOT NULL,
    residence_address BYTEA NOT NULL,
    nationality VARCHAR(50) NOT NULL,
    blood_type VARCHAR(5) NOT NULL
);

CREATE TABLE students (
    id SERIAL PRIMARY KEY,
    document_number BYTEA NOT NULL,
    full_name BYTEA NOT NULL,
    email BYTEA NOT NULL,
    age INTEGER NOT NULL,
    residence_address BYTEA NOT NULL,
    nationality VARCHAR(50) NOT NULL,
    blood_type VARCHAR(5) NOT NULL
);
ALTER TABLE notes ADD FOREIGN KEY (id_professor) REFERENCES teachers(id);
ALTER TABLE notes ADD FOREIGN KEY (id_alumno) REFERENCES students(id);
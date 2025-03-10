CREATE TABLE owners (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    phone VARCHAR(20),
    email VARCHAR(255)
);


CREATE TABLE animals ( 
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    species VARCHAR(50) NOT NULL CHECK (species IN ('horse', 'dog', 'cat', 'sheep', 'chicken', 'rabbit')),
    birth_year INTEGER NOT NULL,
    owner_id INTEGER NOT NULL REFERENCES owners(id) ON DELETE CASCADE,
    notes TEXT
);

CREATE TABLE horses (
    id SERIAL PRIMARY KEY,
    animal_id INTEGER NOT NULL REFERENCES animals(id) ON DELETE CASCADE,
    breed VARCHAR(100),
    color VARCHAR(100),
    training_level INTEGER CHECK (training_level >= 0 and training_level <= 2 ),
    is_available BOOLEAN DEFAULT TRUE
);

CREATE TABLE lessons (
    id SERIAL PRIMARY KEY,
    horse_id INTEGER NOT NULL REFERENCES horses(id) ON DELETE CASCADE,
    date DATE NOT NULL,
    duration FLOAT NOT NULL CHECK (duration > 0),
    price DECIMAL(10, 2) NOT NULL CHECK (price >= 0),
    student_name VARCHAR(255) NOT NULL,
    notes TEXT
)
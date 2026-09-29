DROP TABLE IF EXISTS users;

CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username VARCHAR NOT NULL UNIQUE,
    email VARCHAR NOT NULL UNIQUE,
    age INT
);

INSERT INTO users (username, email, age)
VALUES
    ('john_doe', 'john.doe@example.com', 30),
    ('igorchornyi', 'igorchornyi19@gmail.com', 25),
    ('alex_smith', 'alex.smith@example.com', 22),
    ('maria_k', 'maria.k@example.com', 28),
    ('dmitry_v', 'dmitry.v@example.com', 34),
    ('elena_ro', 'elena.ro@example.com', 29),
    ('sergey_p', 'sergey.p@example.com', 19),
    ('anna_art', 'anna.art@example.com', 27),
    ('pavel_tech', 'pavel.tech@example.com', 31),
    ('olga_web', 'olga.web@example.com', 24),
    ('maxim_coder', 'maxim.coder@example.com', 26),
    ('kate_miller', 'kate.miller@example.com', 23),
    ('roman_boss', 'roman.boss@example.com', 40),
    ('julia_sun', 'julia.sun@example.com', 21),
    ('andrew_sky', 'andrew.sky@example.com', 33),
    ('victoria_m', 'victoria.m@example.com', 35),
    ('denis_fox', 'denis.fox@example.com', 20),
    ('sofia_moon', 'sofia.moon@example.com', 22),
    ('artem_dev', 'artem.dev@example.com', 28),
    ('daria_snow', 'daria.snow@example.com', 26),
    ('vlad_speed', 'vlad.speed@example.com', 32),
    ('irina_star', 'irina.star@example.com', 30),
    ('anton_data', 'anton.data@example.com', 37),
    ('natalia_k', 'natalia.k@example.com', 25),
    ('ivan_rock', 'ivan.rock@example.com', 29),
    ('tatiana_g', 'tatiana.g@example.com', 36),
    ('gleb_design', 'gleb.design@example.com', 23),
    ('oksana_pro', 'oksana.pro@example.com', 31),
    ('nikita_fit', 'nikita.fit@example.com', 27),
    ('alina_flow', 'alina.flow@example.com', 24);
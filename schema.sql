DROP TABLE IF EXISTS restaurants;

CREATE TABLE restaurants (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    restaurant TEXT,
    reservation_time TEXT, 
    headcount TEXT,
    adress TEXT,
    price TEXT,
    venmo_id TEXT
);
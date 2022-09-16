DROP TABLE IF EXISTS clients;

CREATE TABLE clients (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT,
    email TEXT, 
    venmo TEXT,
    venmo_pass TEXT,
    restaurant TEXT,
    time_of_reservation TEXT,
    number_of_people TEXT
    
  
);
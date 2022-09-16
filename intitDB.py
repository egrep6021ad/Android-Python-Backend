import sqlite3

connection = sqlite3.connect('database.db')

with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute(
    "INSERT INTO clients (username, email, venmo, venmo_pass, restaurant, time_of_reservation, number_of_people) VALUES (?,?,?,?,?,?,?)",
    ('Khal', 'khal@gmail.com', 'moneyman', '105g#4w',
     "Applebess", "9pm", "4 people"))

connection.commit()
connection.close()

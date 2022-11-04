from flask import Flask, request, render_template, jsonify
from flask_cors import CORS
from threading import Thread
import sqlite3
import sys
import os
import cryptocode

# Init. flask
app = Flask('')
# Cross origin
CORS(app)
os.environ['TZ'] = ('US/EASTERN')


# Module: Init.sql
def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn


# Module to encrypt:
def encrypt(arg):
    _1_ = os.environ['horcrux_1']
    encoded = cryptocode.encrypt(arg, _1_)
    return encoded


# CREATE listing API Enpoint:
@app.route('/create/', methods=('GET', 'POST'), strict_slashes=False)
def sell_reservation():
    # Parse JSON data:
    data = request.get_json()
    restaurant = data['restaurant']
    time = data['time']
    headcount = data['headcount']
    adress = data['adress']
    price = data['price']
    venmo_id = data['venmo_id']
    # Clean data:
    print(data)
  
    # Insert into Database:
    conn = get_db_connection()
    conn.execute(
        "INSERT INTO restaurants (restaurant, reservation_time, headcount, adress, price, venmo_id) VALUES(?,?,?,?,?,?)",
        (restaurant, time, headcount, adress, price, venmo_id))
    conn.commit()
    conn.close()

    return "[SUCESS] POST"


# GET listing's API Enpoint:
@app.route('/fetch/', methods=['GET'], strict_slashes=False)
def get_reservations():
    conn = get_db_connection()
    # Get all current reservations from DB:
    reservations = conn.execute("SELECT * FROM clients").fetchall()
    conn.close()
    # Build array of objects:
    json = []
    for res in reservations:
        temp = {
            "username": res['username'],
            "email": res['email'],
            "venmo": res['venmo']
        }
        json.append(temp)
    # Return JSON
    return jsonify(json)


# WEB Endpoint (Admin Console)
@app.route('/')
def index():
    conn = get_db_connection()
    restaurants = conn.execute('SELECT * FROM restaurants').fetchall()
    conn.close()
    return render_template('admin_access.html', restaurants=restaurants)


app.run(host='0.0.0.0', port=81)

from flask import Flask, request, render_template, jsonify
from flask_cors import CORS
from threading import Thread
import sqlite3
import sys
import os

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

# Module to encrypt Venmo ID's and Passwords:

# Mobile Endpoint: 

# Query All Current Listings:

# CREATE listing API Enpoint:
@app.route('/create/', methods=('GET', 'POST'), strict_slashes=False)
def sell_reservation():
  data = request.get_json()
  username = data['username']
  email = data['email']
  venmo = data['venmo_id']
  venmo_pass = data['venmo_pass']
  restaurant = data['restaurant']
  time_of_reservation = data['time_of_reservation']
  number_of_people = data['number_of_people']
  

  conn = get_db_connection()
  conn.execute("INSERT INTO clients (username, email, venmo, venmo_pass, restaurant, time_of_reservation, number_of_people) VALUES(?,?,?,?,?,?,?)", (username, email, venmo, venmo_pass, restaurant, time_of_reservation, number_of_people))
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
      "username" : res['username'] ,
      "email" : res['email'] ,
      "venmo" : res['venmo']
    }
    json.append(temp)
  # Return JSON  
  return jsonify(json)


# WEB Endpoint
@app.route('/')
def index():
    conn = get_db_connection()
    clients = conn.execute('SELECT * FROM clients').fetchall()
    conn.close()
    return render_template('admin_access.html', clients=clients)


app.run(host='0.0.0.0', port=81)

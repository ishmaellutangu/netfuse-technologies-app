from flask import Flask, flash, redirect, render_template, request, session
from flaskext.mysql import MySQL

# Configure application
app = Flask(__name__)
mysql = MySQL(app)

import mysql.connector

conn = mysql.connector.connect(
    host='localhost',
    user='your_username',
    password='your_password',
    database='your_database'
)
print("Connected successfully!")

@app.route("/")
def singup():
    return render_template("login.html")
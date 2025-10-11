from flask import Flask, flash, redirect, render_template, request, session
import sqlite3  # For SQLite databases

# Connect to database
db = sqlite3.connect('database.db')

# Configure application
app = Flask(__name__)

@app.route("/")
def singup():
    return render_template("login.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        email_address = request.form.get("email")
        
        # Fixed: Pass parameters as a tuple
        db.execute("INSERT INTO users (username, email) VALUES (?, ?)", 
                  (username, email_address))
        
        db.commit()
        return redirect("/")
    
    return render_template("login.html")
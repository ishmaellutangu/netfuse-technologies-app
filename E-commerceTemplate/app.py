import sqlite3
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route("/")
def singup():
    return render_template("login.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        email_address = request.form['email']

        # Open the connection here (inside the route)
        db = sqlite3.connect('database.db')
        cursor = db.cursor()
        
        try:
            # Check if email already exists
            cursor.execute("SELECT id FROM users WHERE email = ?", (email_address,))
            existing_user = cursor.fetchone()
            
            if existing_user:
                db.close()
                return "This email is already registered. Please use a different email or login."
            
            # Insert new user
            cursor.execute("INSERT INTO users (username, email) VALUES (?, ?)", (username, email_address))
            db.commit()
            db.close()
            return redirect('index.html')
            
        except Exception as e:
            db.close()
            return f"Error: {str(e)}"
    
    return render_template('layout.html')

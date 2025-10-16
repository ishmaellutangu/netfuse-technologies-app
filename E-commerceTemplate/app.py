import sqlite3
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route("/")
def singup():
    return render_template("login.html")
#route for dashboard
@app.route("/item")
def additem():
    return render_template("index.html")
#route for signin page
@app.route('/signinto', methods=['GET', 'POST'])
def signinroute():
     return render_template("signin.html")


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
            return  render_template('signin.html')

            
        except Exception as e:
            db.close()
            return f"Error: {str(e)}"
    
    return render_template('login.html')

#login verifcation

@app.route('/signin', methods=['GET', 'POST'])
def signin():
    if request.method == 'POST':
        username = request.form['username']
        email_address = request.form['email']

        # Open connection safely
        with sqlite3.connect('database.db') as db:
            cursor = db.cursor()

            # Check if user exists
            cursor.execute("SELECT * FROM users WHERE username = ? AND email = ?", (username, email_address))
            existing_user = cursor.fetchone()

        if existing_user:
            # User found — maybe redirect to add page
             return render_template('index.html')
        else:
            # User not found — reload signin page with message
            return render_template('signin.html', error='Invalid username or email')

    # For GET request (just show the signin page)
    return render_template(' signin.html')

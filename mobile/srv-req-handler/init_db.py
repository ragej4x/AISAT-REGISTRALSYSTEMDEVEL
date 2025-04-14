from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

# Database setup
DATABASE = 'database.db'

def init_db():
    with sqlite3.connect(DATABASE) as conn:
        c = conn.cursor()
        # Create table with username, password, and email_id
        c.execute('''CREATE TABLE IF NOT EXISTS users (
                        id INTEGER PRIMARY KEY,
                        username TEXT,
                        password TEXT,
                        email_id TEXT)''')
        conn.commit()

# Route to insert a user into the database
@app.route('/add_user', methods=['POST'])
def add_user():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    email_id = data.get('email_id')

    if not username or not password or not email_id:
        return jsonify({"error": "All fields (username, password, email_id) are required"}), 400

    with sqlite3.connect(DATABASE) as conn:
        c = conn.cursor()
        c.execute('INSERT INTO users (username, password, email_id) VALUES (?, ?, ?)', 
                  (username, password, email_id))
        conn.commit()

    return jsonify({"message": "User added"}), 201

# Route to retrieve all users
@app.route('/users', methods=['GET'])
def get_users():
    with sqlite3.connect(DATABASE) as conn:
        c = conn.cursor()
        c.execute('SELECT * FROM users')
        users = c.fetchall()
    
    return jsonify({"users": users})




@app.route('/login', methods=['POST'])
def login():
    # Get the submitted data from the form
    username = request.form.get('name')
    email = request.form.get('email')
    password = request.form.get('password')

    # Connect to the database and check the credentials
    with sqlite3.connect(DATABASE) as conn:
        c = conn.cursor()
        # Query to find a user with the provided ID No. and email
        c.execute('SELECT * FROM users WHERE username = ? AND email_id = ?', (username, email))
        user = c.fetchone()

        # Check if a user was found and if the password matches
        if user and user[2] == password:  # Assuming user[2] is the password column
            return jsonify({"message": "Login successful"}), 200
        else:
            return jsonify({"error": "Invalid credentials"}), 400



if __name__ == '__main__':
    init_db()  # Initialize the database when the server starts
    app.run(debug=True)

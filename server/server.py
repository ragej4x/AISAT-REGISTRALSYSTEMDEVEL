from flask import Flask, request, jsonify
from flask_cors import CORS
import mysql.connector
from mail_handler import Generatecode

app = Flask(__name__)
CORS(app)

# MySQL connection
db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',  
    database='aisat_registral_db' 
)

cursor = db.cursor()

@app.route('/api/test', methods=['GET'])
def test():
    return jsonify({'message': 'powta active na'})


@app.route('/api/register', methods=['POST'])
def register():
    data = request.json
    level = data.get('level')
    name = data.get('name')
    course = data.get('course')
    idno = data.get('idno')
    cell = data.get('cell')
    email = data.get('email')
    password = data.get('password')

    print('Received data:', data)

    if level == 'College':
        sql = """INSERT INTO users (level, name, course, strand, idno, cell, email, password)
                 VALUES (%s, %s, %s, NULL, %s, %s, %s, %s)"""
        values = (level, name, course, idno, cell, email, password)
    elif level == 'SHS':
        sql = """INSERT INTO users (level, name, course, strand, idno, cell, email, password)
                 VALUES (%s, %s, NULL, %s, %s, %s, %s, %s)"""
        values = (level, name, course, idno, cell, email, password)
    else:
        return jsonify({'message': 'Invalid level selected'}), 400

    try:
        cursor.execute(sql, values)
        db.commit()
        return jsonify({'message': 'User Registered', 'id': cursor.lastrowid})
    except mysql.connector.Error as err:
        print('Register Error:', err)
        return jsonify({'message': 'Server Error'}), 500


@app.route('/api/login', methods=['POST'])
def login():
    data = request.json
    idno = data.get('idno')
    password = data.get('password')

    if not idno or not password:
        return jsonify({'message': 'ID number and password are required'}), 400

    try:
        cursor.execute("SELECT * FROM users WHERE idno = %s", (idno,))
        user = cursor.fetchone()

        if user:
            db_password = user[8] 
            if password == db_password:
                user_data = {
                    'id': user[0],
                    'level': user[1],
                    'name': user[2],
                    'email': user[6]
                }
                return jsonify({'message': 'Login successful', 'user': user_data}), 200
            else:
                return jsonify({'message': 'Wrong password'}), 401
        else:
            return jsonify({'message': 'User not found'}), 404
    except mysql.connector.Error as err:
        print('Login Error:', err)
        return jsonify({'message': 'Server error'}), 500


@app.route('/api/generate', methods=['POST'])
def generate():
    email = request.form.get('email')
    generate = Generatecode(email, attempt=0).get_code()
    print('Generated code:', generate)
    return jsonify({'message': generate})




@app.route('/api/calendar', methods=['GET'])
def get_calendar():
    try:
        cursor.execute("SELECT date, status FROM schedule")
        rows = cursor.fetchall()
        data = {row[0].isoformat(): row[1] for row in rows}
        return jsonify(data)
    except mysql.connector.Error as err:
        print('Fetch Calendar Error:', err)
        return jsonify({'message': 'Server error'}), 500


@app.route('/api/calendar', methods=['POST'])
def update_calendar():
    data = request.json
    date = data['date']
    status = data['status']

    cursor.execute("SELECT id FROM schedule WHERE date = %s", (date,))
    exists = cursor.fetchone()

    if exists:
        cursor.execute("UPDATE schedule SET status = %s WHERE date = %s", (status, date))
    else:
        cursor.execute("INSERT INTO schedule (date, status) VALUES (%s, %s)", (date, status))

    db.commit()
    return jsonify({'message': 'Updated'})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=3000, debug=True)


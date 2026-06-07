from flask import Flask, render_template, request, redirect
from datetime import datetime
import sqlite3
from database import create_table

app = Flask(__name__)
create_table()

def connect_db():
    return sqlite3.connect('parking.db')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/entry', methods=['GET', 'POST'])
def entry():
    if request.method == 'POST':
        data = request.form
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute('''
        INSERT INTO parking 
        (user_type, category, name, vehicle_number, class, division, entry_time, date, paid)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            data['user_type'],
            data['category'],
            data['name'],
            data['vehicle_number'],
            data['class'],
            data['division'],
            datetime.now().strftime("%H:%M"),
            datetime.now().strftime("%Y-%m-%d"),
            1
        ))
        conn.commit()
        conn.close()
        return redirect('/records')
    return render_template('entry.html')

@app.route('/exit', methods=['GET', 'POST'])
def exit():
    if request.method == 'POST':
        vehicle_number = request.form['vehicle_number']
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute('''
        UPDATE parking SET exit_time=? 
        WHERE vehicle_number=? AND exit_time IS NULL
        ''', (
            datetime.now().strftime("%H:%M"),
            vehicle_number
        ))
        conn.commit()
        conn.close()
        return redirect('/records')
    return render_template('exit.html')

@app.route('/records')
def records():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM parking")
    data = cursor.fetchall()
    conn.close()
    return render_template('records.html', records=data)

if __name__ == '__main__':
    app.run(debug=True)

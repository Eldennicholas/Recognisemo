import sqlite3

def connect():
    return sqlite3.connect("data.db", check_same_thread=False)

def register_user(username, email, password):
    conn = connect()
    c = conn.cursor()
    c.execute("INSERT INTO users (username, email, password) VALUES (?, ?, ?)", (username, email, password))
    conn.commit()
    conn.close()

def login_user(email, password):
    conn = connect()
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE email = ? AND password = ?", (email, password))
    result = c.fetchone()
    conn.close()
    return result

def save_mood(username, mood):
    conn = connect()
    c = conn.cursor()
    c.execute("INSERT INTO mood_history (username, mood) VALUES (?, ?)", (username, mood))
    conn.commit()
    conn.close()

def get_mood_history(username):
    conn = connect()
    c = conn.cursor()
    c.execute("SELECT date, mood FROM mood_history WHERE username = ? ORDER BY date DESC LIMIT 15", (username,))
    rows = c.fetchall()
    conn.close()
    return rows[::-1]

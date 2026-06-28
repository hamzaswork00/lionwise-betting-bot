import sqlite3
from datetime import datetime

conn = sqlite3.connect('bot_data.db', check_same_thread=False)
c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS users (
    telegram_id INTEGER PRIMARY KEY,
    username TEXT,
    first_name TEXT,
    language TEXT DEFAULT 'fr',
    status TEXT DEFAULT 'pending',
    account_1xbet TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    activated_at TIMESTAMP
)''')

c.execute('''CREATE TABLE IF NOT EXISTS deposits (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    file_id TEXT,
    status TEXT DEFAULT 'pending',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)''')

c.execute('''CREATE TABLE IF NOT EXISTS predictions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    match TEXT,
    prediction TEXT,
    confidence INTEGER,
    odds TEXT,
    analysis TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)''')

c.execute('''CREATE TABLE IF NOT EXISTS history (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    action TEXT,
    details TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)''')
conn.commit()

def get_user(uid):
    c.execute("SELECT * FROM users WHERE telegram_id=?", (uid,))
    return c.fetchone()

def create_user(uid, username, first_name):
    c.execute("INSERT OR IGNORE INTO users (telegram_id, username, first_name) VALUES (?,?,?)", (uid, username, first_name))
    conn.commit()

def update_user_status(uid, status):
    c.execute("UPDATE users SET status=? WHERE telegram_id=?", (status, uid))
    if status == "active":
        c.execute("UPDATE users SET activated_at=CURRENT_TIMESTAMP WHERE telegram_id=?", (uid,))
    conn.commit()

def set_language(uid, lang):
    c.execute("UPDATE users SET language=? WHERE telegram_id=?", (lang, uid))
    conn.commit()

def add_deposit(uid, file_id):
    c.execute("INSERT INTO deposits (user_id, file_id) VALUES (?,?)", (uid, file_id))
    conn.commit()
    return c.lastrowid

def get_deposit(dep_id):
    c.execute("SELECT * FROM deposits WHERE id=?", (dep_id,))
    return c.fetchone()

def update_deposit_status(dep_id, status):
    c.execute("UPDATE deposits SET status=? WHERE id=?", (status, dep_id))
    conn.commit()

def add_prediction(uid, match, prediction, confidence, odds, analysis):
    c.execute("INSERT INTO predictions (user_id, match, prediction, confidence, odds, analysis) VALUES (?,?,?,?,?,?)",
              (uid, match, prediction, confidence, odds, analysis))
    conn.commit()

def get_user_predictions(uid, limit=10):
    c.execute("SELECT * FROM predictions WHERE user_id=? ORDER BY created_at DESC LIMIT ?", (uid, limit))
    return c.fetchall()

def get_stats():
    total = c.execute("SELECT COUNT(*) FROM users").fetchone()[0]
    pending = c.execute("SELECT COUNT(*) FROM users WHERE status='pending'").fetchone()[0]
    active = c.execute("SELECT COUNT(*) FROM users WHERE status='active'").fetchone()[0]
    banned = c.execute("SELECT COUNT(*) FROM users WHERE status='banned'").fetchone()[0]
    return total, pending, active, banned

def add_history(uid, action, details=""):
    c.execute("INSERT INTO history (user_id, action, details) VALUES (?,?,?)", (uid, action, details))
    conn.commit()

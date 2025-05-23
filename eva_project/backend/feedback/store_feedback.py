# 📁 eva/backend/feedback/store_feedback.py
import sqlite3
from datetime import datetime

def init_db():
    conn = sqlite3.connect("feedback.db")
    cur = conn.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS feedback (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        question TEXT,
        answer TEXT,
        rating TEXT,
        user_email TEXT,
        timestamp TEXT
    )
    """)
    conn.commit()
    conn.close()

def save_feedback(question, answer, rating, user_email):
    conn = sqlite3.connect("feedback.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO feedback (question, answer, rating, user_email, timestamp) VALUES (?, ?, ?, ?, ?)",
                (question, answer, rating, user_email, datetime.utcnow().isoformat()))
    conn.commit()
    conn.close()# Dummy content for store_feedback.py

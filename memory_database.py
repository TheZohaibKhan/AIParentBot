# memory_database.py

import sqlite3
from datetime import datetime

# Initialize database (renamed to match your main.py)
def init_memory():
    conn = sqlite3.connect("conversation_memory.db")
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS conversations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            user_text TEXT,
            emotion TEXT,
            bot_reply TEXT
        )
    ''')
    conn.commit()
    conn.close()

# Save a conversation
def save_conversation(user_text, emotion, bot_reply):
    conn = sqlite3.connect("conversation_memory.db")
    cursor = conn.cursor()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cursor.execute('''
        INSERT INTO conversations (timestamp, user_text, emotion, bot_reply)
        VALUES (?, ?, ?, ?)
    ''', (timestamp, user_text, emotion, bot_reply))
    conn.commit()
    conn.close()

# View past conversations
def get_from_memory():
    conn = sqlite3.connect("conversation_memory.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM conversations ORDER BY id DESC LIMIT 10")
    rows = cursor.fetchall()
    conn.close()
    return rows

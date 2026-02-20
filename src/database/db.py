import sqlite3

class DatabaseManager:
    def __init__(self, db_path="crypto_safe.db"):
        self.conn = sqlite3.connect(db_path)
        self.create_tables()

    def create_tables(self):
        cursor = self.conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS audit_log (
                id INTEGER PRIMARY KEY,
                action TEXT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                entry_id INTEGER,
                details TEXT,
                signature TEXT
            )
        ''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS key_store (
                id INTEGER PRIMARY KEY,
                key_type TEXT,
                salt BLOB,
                hash BLOB,
                params TEXT
            )
        ''')
        #таблица паролей
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS vault_entries (
                id INTEGER PRIMARY KEY,
                title TEXT,
                username TEXT,
                encrypted_password TEXT,
                url TEXT,
                notes TEXT,
                tags TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        #таблица настроек
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS settings (
                id INTEGER PRIMARY KEY,
                setting_key TEXT UNIQUE,
                setting_value TEXT
            )
        ''')
        self.conn.commit()

    def add_entry(self, title, username, password):
        cursor = self.conn.cursor()
        cursor.execute(
            "INSERT INTO vault_entries (title, username, encrypted_password) VALUES (?, ?, ?)",
            (title, username, password)
        )
        self.conn.commit()
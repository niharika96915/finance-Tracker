from datetime import datetime

class TransactionManager:
    def __init__(self, db):
        self.db = db

    def add_transaction(self, category, description, amount, type_):
        date = datetime.now().strftime('%Y-%m-%d')
        self.db.cursor.execute('''
            INSERT INTO transactions (date, category, description, amount, type)
            VALUES (?, ?, ?, ?, ?)
        ''', (date, category, description, amount, type_))
        self.db.conn.commit()

    def get_balance(self):
        self.db.cursor.execute('''
            SELECT SUM(CASE WHEN type = 'income' THEN amount ELSE -amount END)
            FROM transactions
        ''')
        balance = self.db.cursor.fetchone()[0] or 0
        return balance

    def get_transactions(self):
        self.db.cursor.execute('SELECT * FROM transactions ORDER BY date DESC')
        return self.db.cursor.fetchall()
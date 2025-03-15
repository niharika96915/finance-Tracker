import sqlite3

class CategoryManager:
    def __init__(self, db):
        self.db = db
        self._initialize_default_categories()

    def _initialize_default_categories(self):
        default_categories = {
            'income': ['Salary', 'Freelance', 'Investments', 'Other Income'],
            'expense': ['Food', 'Transport', 'Utilities', 'Entertainment', 'Shopping']
        }
        
        for type_, categories in default_categories.items():
            for category in categories:
                try:
                    self.db.cursor.execute('INSERT INTO categories (name, type) VALUES (?, ?)',
                                      (category, type_))
                except sqlite3.IntegrityError:
                    pass
        self.db.conn.commit()

    # ... rest of the code remains the same ...
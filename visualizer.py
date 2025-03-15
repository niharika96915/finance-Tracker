import matplotlib.pyplot as plt

class Visualizer:
    def __init__(self, db):
        self.db = db

    def visualize_expenses(self):
        self.db.cursor.execute('''
            SELECT category, SUM(amount) 
            FROM transactions 
            WHERE type = 'expense'
            GROUP BY category
        ''')
        data = self.db.cursor.fetchall()
        
        if not data:
            print("No expense data to visualize!")
            return
            
        categories, amounts = zip(*data)
        plt.figure(figsize=(10, 6))
        plt.pie(amounts, labels=categories, autopct='%1.1f%%')
        plt.title('Expense Distribution by Category')
        plt.axis('equal')
        plt.show()
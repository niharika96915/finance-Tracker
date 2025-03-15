import csv
import json
from datetime import datetime

class ExportManager:
    def __init__(self, db):
        self.db = db

    def export_to_csv(self, filename=None):
        if filename is None:
            filename = f"finance_export_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
        
        self.db.cursor.execute('SELECT * FROM transactions ORDER BY date DESC')
        transactions = self.db.cursor.fetchall()
        
        with open(filename, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['ID', 'Date', 'Category', 'Description', 'Amount', 'Type'])
            writer.writerows(transactions)
        
        return filename

    def export_to_json(self, filename=None):
        if filename is None:
            filename = f"finance_export_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        
        self.db.cursor.execute('SELECT * FROM transactions ORDER BY date DESC')
        transactions = self.db.cursor.fetchall()
        
        data = []
        for t in transactions:
            data.append({
                'id': t[0],
                'date': t[1],
                'category': t[2],
                'description': t[3],
                'amount': t[4],
                'type': t[5]
            })
        
        with open(filename, 'w') as jsonfile:
            json.dump(data, jsonfile, indent=4)
        
        return filename
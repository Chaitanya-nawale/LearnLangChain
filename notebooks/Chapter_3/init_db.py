import sqlite3

conn = sqlite3.connect('SalesDB/sales.db')

cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS sales (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_name TEXT NOT NULL,
    quantity INTEGER NOT NULL,
    price REAL NOT NULL,
    sale_date TEXT NOT NULL
)''')

cursor.execute('''
INSERT INTO sales (product_name, quantity, price, sale_date)
VALUES
    ('Widget A', 10, 19.99, '2023-01-15'),
    ('Widget B', 5, 29.99, '2023-01-16'),
    ('Widget C', 8, 9.99, '2023-01-17'),
    ('Widget D', 12, 14.99, '2023-01-18'),
    ('Widget E', 7, 24.99, '2023-01-19')
''')

conn.commit()
conn.close()

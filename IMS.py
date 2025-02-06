import sqlite3


def create_table():
    conn = sqlite3.connect('inventory.db')
    cursor=conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS inventory (
            item_id INTEGER PRIMARY KEY,
            item_name TEXT NOT NULL,
            quantity INTEGER NOT NULL,
            price REAL NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def fetch_product():
    conn=sqlite3.connect('inventory.db')
    cursor=conn.cursor()
    cursor.execute('SELECT * FROM inventory')
    inventory=cursor.fetchall()
    conn.close()
    return inventory

def insert_Product(item_id, item_name, quantity, price):
    conn = sqlite3.connect('inventory.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO inventory (item_id, item_name, quantity, price) VALUES (?,?,?,?)', (item_id, item_name, quantity, price))
    conn.commit()
    conn.close()

def delete_Product(item_id):
    conn=sqlite3.connect('inventory.db')
    cursor=conn.cursor()
    cursor.execute('DELETE from inventory WHERE item_id =?',(item_id,))
    conn.commit()
    conn.close()

def update_Product(item_name, quantity, price, item_id):
    conn=sqlite3.connect('inventory.db')
    cursor=conn.cursor()
    cursor.execute('UPDATE inventory  SET item_name = ?, quantity = ?, price = ? WHERE item_id = ?',(item_name, quantity, price, item_id))
    conn.commit()
    conn.close()


def id_exists(item_id):
     conn =sqlite3.connect('inventory.db')
     cursor=conn.cursor()
     cursor.execute('SELECT COUNT(*) FROM inventory WHERE item_id = ?',(item_id,))
     result=cursor.fetchone()
     conn.close()
     return result [0] > 0

create_table()


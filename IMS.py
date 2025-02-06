import sqlite3

def create_table():
    conn = sqlite3.connect('inventory.db')
    cursor=conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS inventory(
               id TEXT PRIMARY KEY,
               name TEXT,
               in_stock INTEGER,
               price REAL)'''

)
    conn.commit()
    conn.close()

def fetch_product():
    conn=sqlite3.connect('inventory.db')
    cursor=conn.cursor()
    cursor.execute('SELECT * FROM inventory')
    inventory=cursor.fetchall()
    conn.close()
    return inventory

def insert_Product(id, name, stock, price):
    conn = sqlite3.connect('inventory.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO inventory (id, name, in_stock, price) VALUES (?,?,?,?)', (id, name, stock, price))
    conn.commit()
    conn.close()

def delete_Product(id):
    conn=sqlite3.connect('inventory.db')
    cursor=conn.cursor()
    cursor.execute('DELETE from inventory WHERE id =?',(id,))
    conn.commit()
    conn.close()

def update_Product(name, stock, price, id):
    conn=sqlite3.connect('inventory.db')
    cursor=conn.cursor()
    cursor.execute('UPDATE inventory  SET name = ?, in_stock = ?, price = ? WHERE id = ?',(name, stock, price, id))
    conn.commit()
    conn.close()


def id_exists(id):
     conn =sqlite3.connect('inventory.db')
     cursor=conn.cursor()
     cursor.execute('SELECT COUNT(*) FROM inventory WHERE id = ?',(id,))
     result=cursor.fetchone()
     conn.close
     return result[0]>0
create_table()

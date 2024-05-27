import sqlite3

def connect():
    conn = sqlite3.connect('clientes.db')
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS clientes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        apellido TEXT NOT NULL,
        sexo TEXT NOT NULL
    )
    ''')
    conn.commit()
    conn.close()

def insert(nombre, apellido, sexo):
    conn = sqlite3.connect('clientes.db')
    cursor = conn.cursor()
    cursor.execute('''
    INSERT INTO clientes (nombre, apellido, sexo)
    VALUES (?, ?, ?)
    ''', (nombre, apellido, sexo))
    conn.commit()
    conn.close()

def update(id, nombre, apellido, sexo):
    conn = sqlite3.connect('clientes.db')
    cursor = conn.cursor()
    cursor.execute('''
    UPDATE clientes
    SET nombre = ?, apellido = ?, sexo = ?
    WHERE id = ?
    ''', (nombre, apellido, sexo, id))
    conn.commit()
    conn.close()

def delete(id):
    conn = sqlite3.connect('clientes.db')
    cursor = conn.cursor()
    cursor.execute('''
    DELETE FROM clientes
    WHERE id = ?
    ''', (id,))
    conn.commit()
    conn.close()

def fetch_all():
    conn = sqlite3.connect('clientes.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM clientes')
    rows = cursor.fetchall()
    conn.close()
    return rows

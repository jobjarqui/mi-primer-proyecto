import sqlite3

def connect():
    conn = sqlite3.connect('recetas.db')
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS recetas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        ingredientes TEXT NOT NULL,
        intrucciones TEXT NOT NULL,
        tiempo TEXT NOT NULL
    )
    ''')
    conn.commit()
    conn.close()

def insert(nombre, ingredientes, instrucciones, tiempo):
    conn = sqlite3.connect('recetas.db')
    cursor = conn.cursor()
    cursor.execute('''
    INSERT INTO recetas (nombre, ingredientes, intrucciones, tiempo)
    VALUES (?, ?, ?, ?)
    ''', (nombre, ingredientes, instrucciones, tiempo))
    conn.commit()
    conn.close()

def update(id, nombre, ingredientes, intrucciones, tiempo):
    conn = sqlite3.connect('recetas.db')
    cursor = conn.cursor()
    cursor.execute('''
    UPDATE recetas
    SET nombre = ?, ingredientes = ?, intrucciones = ?, tiempo = ?
    WHERE id = ?
    ''', (nombre, ingredientes, intrucciones, tiempo, id))
    conn.commit()
    conn.close()

def delete(id):
    conn = sqlite3.connect('recetas.db')
    cursor = conn.cursor()
    cursor.execute('''
    DELETE FROM recetas
    WHERE id = ?
    ''', (id,))
    conn.commit()
    conn.close()

def fetch_all():
    conn = sqlite3.connect('recetas.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM recetas')
    rows = cursor.fetchall()
    conn.close()
    return rows

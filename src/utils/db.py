"""Módulo con funciones para interactuar con la base de datos."""

# Importar módulos

import sqlite3
import os

# Constantes

DIR_SQL = os.path.join(os.path.dirname(__file__), "sql", "poblado_bd.sql")

# Funciones

def crear_db():
    """Crea la base de datos del juego.
    """
    conexion = sqlite3.connect("ahorcado.db")
    cursor = conexion.cursor()
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS JUGADOR (
        id INTEGER PRIMARY KEY,
        nick TEXT NOT NULL UNIQUE,
        email TEXT NOT NULL UNIQUE,
        puntaje_max INTEGER NOT NULL DEFAULT 0
    )
    """)
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS CATEGORIA (
        id INTEGER PRIMARY KEY,
        nombre TEXT NOT NULL UNIQUE
    )
    """)
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS PALABRA (
        id INTEGER PRIMARY KEY,
        nombre TEXT NOT NULL UNIQUE,
        categoria_id INTEGER NOT NULL,
        FOREIGN KEY (categoria_id) REFERENCES categorias (id)
    )
    """)
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS JUEGO (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        jugador_id INTEGER NOT NULL,
        categoria_id INTEGER NOT NULL,
        puntaje INTEGER NOT NULL DEFAULT 0,
        intentos INTEGER NOT NULL DEFAULT 0,
        palabra_id INTEGER NOT NULL,
        FOREIGN KEY (jugador_id) REFERENCES jugadores (id),
        FOREIGN KEY (categoria_id) REFERENCES categorias (id),
        FOREIGN KEY (palabra_id) REFERENCES palabras (id)
    )
    """)
    
    conexion.commit()
    conexion.close()


def poblar_bd():
    """Pobla la base de datos con el script sql del archivo 'poblado_bd.sql' ubicado en la carpeta 'sql'."""

    conexion = sqlite3.connect("ahorcado.db")
    cursor = conexion.cursor()

    try:
        with open(DIR_SQL) as archivo:
            script = archivo.read()
            print("Script SQL a ejecutar:\n", script)  # Imprime el script SQL
            cursor.executescript(script)
        conexion.commit()
    except sqlite3.OperationalError as e:
        print(f"Error al ejecutar el script SQL: {e}")
    finally:
        conexion.close()




if __name__ == "__main__":
    crear_db()
    poblar_bd()

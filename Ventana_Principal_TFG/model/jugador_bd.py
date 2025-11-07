import sqlite3
import os

DB_PATH = "jugador.db"

# === CONEXIÓN ===
def get_connection():
    """Devuelve una conexión activa a la base de datos de jugador."""
    return sqlite3.connect(DB_PATH)


# === CREACIÓN DE TABLA ===
def create_table():
    """Crea la tabla de jugador si no existe."""
    if not os.path.exists(DB_PATH):
        conn = sqlite3.connect(DB_PATH)
    else:
        conn = get_connection()

    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS jugador (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT,
            nivel_actual INTEGER,
            tiempo_juego TEXT,
            puntuacion_total INTEGER,
            fecha_guardada TEXT DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()
    print("Tabla 'jugador' creada o ya existente.")



# === CARGAR PARTIDAS ===
def cargar_partidas():
    """Devuelve todas las partidas guardadas ordenadas por ID ascendente."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT id, nombre, nivel_actual, tiempo_juego, puntuacion_total, fecha_guardada
        FROM jugador
        ORDER BY id ASC
    """)
    partidas = cursor.fetchall()
    conn.close()
    return partidas

def eliminar_partida(id_partida):
    """Elimina una partida por su ID."""
    conn = sqlite3.connect("jugador.db")  # o el nombre de tu BD principal
    cursor = conn.cursor()
    cursor.execute("DELETE FROM jugador WHERE id = ?", (id_partida,))
    conn.commit()
    conn.close()
    print(f"Partida {id_partida} eliminada correctamente.")


# === INICIALIZAR BD ===
def inicializar_bd():
    """Inicializa la base de datos de jugador (crea la tabla si no existe)."""
    create_table()

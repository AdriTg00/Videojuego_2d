import sqlite3
import os

# Ruta absoluta a la raíz del proyecto

DB_PATH = os.path.join("configuracion.db")

# === CONEXIÓN ===
def get_connection():
    """Devuelve una conexión activa a la base de datos de configuración."""
    return sqlite3.connect(DB_PATH)


# === CREACIÓN DE TABLA ===
def create_table():
    """Crea la tabla de configuración si no existe."""
    if not os.path.exists(DB_PATH):
        conn = sqlite3.connect(DB_PATH)
    else:
        conn = get_connection()

    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS configuracion (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            volumen_musica INTEGER,
            volumen_sfx INTEGER,
            resolucion TEXT,
            modo_pantalla TEXT
        )
    ''')
    conn.commit()
    conn.close()
    print("✅ Tabla 'configuracion' creada o ya existente.")


# === GUARDAR CONFIGURACIÓN ===
def guardar_configuracion(volumen_musica, volumen_sfx, resolucion, modo_pantalla):
    """Guarda o reemplaza la configuración actual."""
    conn = get_connection()
    cursor = conn.cursor()

    # Eliminamos la anterior para mantener solo una
    cursor.execute("DELETE FROM configuracion")
    cursor.execute("""
        INSERT INTO configuracion (volumen_musica, volumen_sfx, resolucion, modo_pantalla)
        VALUES (?, ?, ?, ?)
    """, (volumen_musica, volumen_sfx, resolucion, modo_pantalla))

    conn.commit()
    conn.close()
    print("Configuración guardada correctamente.")

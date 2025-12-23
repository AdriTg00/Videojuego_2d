from functools import partial
from PySide6.QtCore import Signal
from PySide6.QtWidgets import QWidget, QMessageBox
from views.partidasGuardadas_ui import Ui_partidaGuardada
from translator import TRANSLATIONS
from services.partidaService import PartidasService
from PySide6.QtWidgets import QTableWidgetItem



class cargar(QWidget):
    partida_seleccionada = Signal(int)

    def __init__(self, app_state,  parent=None):
        super().__init__(parent)
        self.ui = Ui_partidaGuardada()
        self.ui.tablaGuardados.itemDoubleClicked.connect(self._on_partida_doble_click)
        self.partida_service = PartidasService()
        self.app_state = app_state
        self.ui.setupUi(self)
        self.apply_language()
        self.cargar_partidas()
    

    def _safe_disconnect(self, widget):
        """Intenta desconectar todas las conexiones en clicked para evitar duplicados."""
        try:
            widget.clicked.disconnect()
        except Exception:
            pass
    
    def apply_language(self):
        """Actualiza todos los textos de la interfaz según el idioma actual."""
        lang = self.app_state.get("language", "Español")
        tr = TRANSLATIONS[lang]

        # Título y etiqueta principal
        self.setWindowTitle(tr.get("saved_games", "Partidas guardadas:"))
        self.ui.partidasGuardadas.setText(tr.get("saved_games", "Partidas guardadas:"))
    def cargar_partidas(self):
        jugador = self.app_state.get("usuario")

        if not jugador:
            QMessageBox.warning(self, "Error", "No hay usuario activo")
            return

        try:
            partidas = self.partida_service.obtener_partidas(jugador)
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))
            return

        tabla = self.ui.tablaGuardados
        tabla.setRowCount(0)

        for fila, partida in enumerate(partidas):
            tabla.insertRow(fila)

            tabla.setItem(fila, 0, QTableWidgetItem(jugador))
            tabla.setItem(fila, 1, QTableWidgetItem(str(partida.nivel)))
            tabla.setItem(fila, 2, QTableWidgetItem(str(partida.muertes_nivel)))
            tabla.setItem(fila, 3, QTableWidgetItem(str(partida.puntuacion)))
            tabla.setItem(fila, 4, QTableWidgetItem(self._formatear_tiempo(partida.tiempo)))

            # Guardamos el ID oculto en la fila
            tabla.item(fila, 0).setData(256, partida.id_partida)
            
    def _formatear_tiempo(self, segundos):
        if not segundos:
            return "00:00"

        minutos = int(segundos) // 60
        seg = int(segundos) % 60
        return f"{minutos:02}:{seg:02}"
    
    def _on_partida_doble_click(self, item):
        fila = item.row()
        item_id = self.ui.tablePartidas.item(fila, 0)
        partida_id = item_id.data(256)

        self.partida_seleccionada.emit(partida_id)
        self.close()





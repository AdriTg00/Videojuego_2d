from functools import partial
from PySide6.QtCore import Signal
from PySide6.QtWidgets import QWidget, QMessageBox
from views.partidasGuardadas_ui import Ui_partidaGuardada
from model.jugador_bd import cargar_partidas, eliminar_partida as eliminar_partida_bd
from translator import TRANSLATIONS


class cargar(QWidget):
    partida_seleccionada = Signal(int)

    def __init__(self, app_state,  parent=None):
        super().__init__(parent)
        self.ui = Ui_partidaGuardada()
        self.app_state = app_state
        self.ui.setupUi(self)
        self.apply_language()
        self.mostrar_partidas()

    def _safe_disconnect(self, widget):
        """Intenta desconectar todas las conexiones en clicked para evitar duplicados."""
        try:
            widget.clicked.disconnect()
        except Exception:
            # Si no tenía conexión o no se puede desconectar, ignoramos
            pass

    def mostrar_partidas(self):
        """Rellena los botones con las partidas guardadas y conecta las X correctamente."""
        partidas = cargar_partidas()

        botones = [
            self.ui.partidaGuardada1,
            self.ui.partidaGuardada2,
            self.ui.partidaGuardada3,
            self.ui.partidaGuardada4,
            self.ui.partidaGuardada5,
            self.ui.partidaGuardada6,
            self.ui.partidaGuardada7,
            self.ui.partidaGuardada8
        ]

        botones_x = [
            self.ui.x1,
            self.ui.x2,
            self.ui.x3,
            self.ui.x4,
            self.ui.x5,
            self.ui.x6,
            self.ui.x7,
            self.ui.x8
        ]

        # Primero desconectamos handlers anteriores (evita duplicados si refrescas la lista)
        for w in botones + botones_x:
            self._safe_disconnect(w)
        
        # Ahora rellenamos y conectamos de forma segura
        for i, boton in enumerate(botones):
            if i < len(partidas):
                id_, nombre, nivel, tiempo, puntuacion, fecha = partidas[i]
                texto = f"{nombre} — Nivel {nivel} — {puntuacion} pts — {tiempo}"
                boton.setText(texto)
                boton.setEnabled(True)

                # Conectamos el click del botón de partida a un handler que recibe el id
                boton.clicked.connect(partial(self._on_partida_clicked, id_))

                # Configuramos el botón X: habilitado y con handler que recibe el id
                botones_x[i].setEnabled(True)
                botones_x[i].clicked.connect(partial(self._confirm_eliminar, id_))

            else:
                boton.setText("<Vacío>")
                boton.setEnabled(False)
                botones_x[i].setEnabled(False)

    # ---------- Handlers ----------
    def _on_partida_clicked(self, id_partida):
        print(f"Partida seleccionada: {id_partida}")
        self.partida_seleccionada.emit(id_partida)
    
    def apply_language(self):
        """Actualiza todos los textos de la interfaz según el idioma actual."""
        lang = self.app_state.get("language", "Español")
        tr = TRANSLATIONS[lang]

        # Título y etiqueta principal
        self.setWindowTitle(tr.get("saved_games", "Partidas guardadas:"))
        self.ui.partidasGuardadas.setText(tr.get("saved_games", "Partidas guardadas:"))

        # Si tienes botones tipo "<Vacío>", actualízalos también:
        # ⚠️ Ajusta los nombres de los botones según los que tengas en el .ui
        for boton in [
            self.ui.x1,
            self.ui.x2,
            self.ui.x3,
            self.ui.x4,
            self.ui.x5,
            self.ui.x6,
            self.ui.x7,
            self.ui.x8
        ]:
            boton.setText(tr.get("empty_slot", "<Vacío>"))


    def _confirm_eliminar(self, id_partida):
        """Muestra confirmación y si confirma elimina la partida por id."""
        if id_partida is None:
            return

        reply = QMessageBox.question(
            self,
            "Eliminar partida",
            "¿Seguro que quieres eliminar esta partida?",
            QMessageBox.Yes | QMessageBox.No
        )

        if reply == QMessageBox.Yes:
            eliminar_partida_bd(id_partida)
            # refrescamos la vista (esto desconectará y volverá a conectar correctamente)
            self.mostrar_partidas()

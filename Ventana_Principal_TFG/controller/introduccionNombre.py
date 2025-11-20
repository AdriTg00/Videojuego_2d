from PySide6.QtCore import Signal
from PySide6.QtWidgets import QWidget, QMessageBox
from views.introduccionNombre_ui import Ui_introduccionNombre
from translator import TRANSLATIONS
from services.jugadorService import JugadorService
from DAO.jugadorDAO import JugadorDAO


class introducirNombre(QWidget):
    nombre_validado = Signal(str)

    def __init__(self, app_state, parent=None):
        super().__init__(parent)
        self.ui = Ui_introduccionNombre()
        self.app_state = app_state
        self.dao = JugadorDAO()
        self.service = JugadorService(self.dao)
        self.ui.setupUi(self)
        self.apply_language()
        self.ui.iniciarPartida.clicked.connect(self.validar_nombre)

    def apply_language(self):
        lang = self.app_state.get("language", "Español")
        tr = TRANSLATIONS[lang]

        self.setWindowTitle(tr["intro_title"])
        self.ui.labelNombre.setText(tr["intro_label"])
        self.ui.iniciarPartida.setText(tr["intro_button"])
        self.ui.nombre.setPlaceholderText(tr["intro_placeholder"])

    def validar_nombre(self):
        nombre = self.ui.nombre.text().strip()

        if not nombre:
            QMessageBox.warning(self, "Error", "El nombre no puede estar vacío.")
            return

        datos = self.service.crear_usuario(nombre)
        user_id = datos["id"]

        # Emitimos el ID (NO el nombre)
        self.nombre_validado.emit(user_id)

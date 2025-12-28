from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QVBoxLayout,
    QFrame
)
from PySide6.QtCore import Qt


class EstadisticasJugadorWidget(QFrame):

    def __init__(self, parent=None):
        super().__init__(parent)

        # -----------------------------
        # Configuración visual
        # -----------------------------
        self.setFrameShape(QFrame.StyledPanel)
        self.setFrameShadow(QFrame.Raised)
        self.setObjectName("estadisticasJugador")

        self.setStyleSheet("""
            QFrame#estadisticasJugador {
                border: 2px solid #8B5A2B;
                background-color: #F5E6C8;
                border-radius: 6px;
            }
            QLabel {
                color: #3A2A1A;
                font-size: 14px;
            }
            QLabel#titulo {
                font-size: 16px;
                font-weight: bold;
            }
        """)

        # -----------------------------
        # Layout
        # -----------------------------
        layout = QVBoxLayout(self)
        layout.setSpacing(6)
        layout.setContentsMargins(12, 10, 12, 10)

        # -----------------------------
        # Labels
        # -----------------------------
        self.lblTitulo = QLabel("📊 Última partida completada")
        self.lblTitulo.setObjectName("titulo")
        self.lblTitulo.setAlignment(Qt.AlignCenter)

        self.lblJugador = QLabel("Jugador: -")
        self.lblTiempo = QLabel("Tiempo total: -")
        self.lblPuntuacion = QLabel("Puntuación total: -")
        self.lblNiveles = QLabel("Niveles superados: -")

        # -----------------------------
        # Añadir al layout
        # -----------------------------
        layout.addWidget(self.lblTitulo)
        layout.addSpacing(6)
        layout.addWidget(self.lblJugador)
        layout.addWidget(self.lblTiempo)
        layout.addWidget(self.lblPuntuacion)
        layout.addWidget(self.lblNiveles)
        self.hide()

    # ==================================================
    # API pública del widget
    # ==================================================

    def cargar_estadisticas(self, data: dict):
        """
        data viene del backend (/jugadores/obtener)

        Ejemplo:
        {
            "nombre": "joseluis",
            "tiempo_total": 105.4,
            "puntuacion_total": 30,
            "niveles_superados": 3
        }
        """

        if not data:
            self.hide()
            return

        self.lblJugador.setText(f"Jugador: {data.get('nombre', '-')}")
        self.lblTiempo.setText(
            f"Tiempo total: {round(data.get('tiempo_total', 0), 2)} s"
        )
        self.lblPuntuacion.setText(
            f"Puntuación total: {data.get('puntuacion_total', 0)}"
        )
        self.lblNiveles.setText(
            f"Niveles superados: {data.get('niveles_superados', 0)}"
        )

        self.show()

    def limpiar(self):
        """Oculta el widget (por ejemplo, si no hay partida completada)."""
        self.hide()

import sys
from PySide6.QtCore import QTranslator, QCoreApplication
from PySide6.QtWidgets import QApplication
from controller.app_controller import AppController
from model.jugador_bd import inicializar_bd
from resources import resources_rc
from model.config_bd import create_table

def main():
    create_table()
    inicializar_bd()      
    app = QApplication(sys.argv)
    app.setApplicationName("Launcher")
    app.setStyleSheet("""
        QMessageBox QLabel {
            color: black;
        }
        QMessageBox QPushButton {
            color: black;
        }
    """)
    controller = AppController()
    controller.launcher.setFixedSize(controller.launcher.size())
    controller.launcher.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
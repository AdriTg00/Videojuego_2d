from .VentanaInicio import launcher
from .cargarPartidas import cargar
from .configuracion import configuracion
from PySide6.QtCore import Qt


class AppController:
    def __init__(self):
        self.app_state = {"language": "Español"}
        self.launcher = launcher(self.app_state)
        self.config_window = configuracion(self.app_state)
        self.carg_partidas = cargar(self.app_state)
        self.launcher.abrir_config_signal.connect(self.mostrar_configuracion)
        self.launcher.abrir_cargar_signal.connect(self.mostrar_partidas_guardadas)
        self.launcher.idioma_cambiado.connect(self.config_window.apply_language)
        self.launcher.idioma_cambiado.connect(self.carg_partidas.apply_language)
    
        

    def mostrar_partidas_guardadas(self):
        print("Abriendo ventana de configuración desde el controlador")
        self.carg_partidas.setWindowModality(Qt.ApplicationModal) 
        self.carg_partidas.show()  
        

    def mostrar_configuracion(self):
        print("Abriendo ventana de cargar partida desde el controlador")
        self.config_window.setWindowModality(Qt.ApplicationModal) 
        self.config_window.show()  
        
    

   
   

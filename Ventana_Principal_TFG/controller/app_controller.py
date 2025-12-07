# app_controller.py  (sustituir el contenido actual por este)
from .VentanaInicio import launcher
from .cargarPartidas import cargar
from .configuracion import configuracion
from .introduccionNombre import introducirNombre
from PySide6.QtCore import Qt
import os
import json


class AppController:
    def __init__(self):
        self.nombre_jugador = None
        self.app_state = {"language": "Español"}
        self.launcher = launcher(self.app_state)
        self.config_window = configuracion(self.app_state)
        self.carg_partidas = cargar(self.app_state)
        self.introducir_nombre = introducirNombre(self.app_state)

        # Conectar señal de nombre_validado desde introducirNombre -> manejador en este controlador.
        # Usamos Qt.QueuedConnection por seguridad si la señal viene de un worker/hilo.
        try:
            self.introducir_nombre.nombre_validado.connect(
                self._on_nombre_validado,
                type=Qt.QueuedConnection
            )
            print("[AppController] Conectada señal nombre_validado -> _on_nombre_validado")
        except Exception as e:
            print("[AppController] ERROR conectando nombre_validado:", e)

        # Conexiones existentes del launcher (las dejamos tal cual)
        self.launcher.abrir_config_signal.connect(self.mostrar_configuracion)
        self.launcher.abrir_cargar_signal.connect(self.mostrar_partidas_guardadas)
        self.launcher.abrir_nueva_signal.connect(self.abrir_nueva_partida)
        self.launcher.idioma_cambiado.connect(self.config_window.apply_language)
        self.launcher.idioma_cambiado.connect(self.carg_partidas.apply_language)
        self.launcher.idioma_cambiado.connect(self.introducir_nombre.apply_language)

        # Comprobar si hay usuario local guardado y mostrar la ventana adecuada
        self.comprobar_usuario_local()


    def mostrar_launcher(self, user_id):
        """
        Preparar y mostrar launcher. Este método se usa tanto cuando el usuario
        ya existía en disco (arranque) como cuando se crea uno nuevo desde introducirNombre.
        """
        print("Usuario validado:", user_id)
        self.user_id = user_id   # Guardar ID en memoria
        self.nombre_jugador = user_id

        # Ocultar la ventana de introducción si sigue abierta
        try:
            if hasattr(self, "introducir_nombre") and self.introducir_nombre:
                # hide() evita forzar destrucción si prefieres reutilizar el widget
                self.introducir_nombre.hide()
        except Exception as e:
            print("[AppController] Error ocultando introducir_nombre:", e)

        # Mostrar launcher (asegurarse)
        try:
            if not self.launcher.isVisible():
                self.launcher.show()
                self.launcher.raise_()
                self.launcher.activateWindow()
        except Exception as e:
            print("[AppController] Error mostrando launcher:", e)
     
        
    def mostrar_partidas_guardadas(self):
        print("Abriendo ventana de configuración desde el controlador")
        self.carg_partidas.setWindowModality(Qt.ApplicationModal) 
        self.carg_partidas.show()  
        

    def mostrar_configuracion(self):
        print("Abriendo ventana de cargar partida desde el controlador")
        self.config_window.setWindowModality(Qt.ApplicationModal) 
        self.config_window.show()  
    
    
    def abrir_nueva_partida(self):
        print("Abriendo ventana de introducción de nombre desde el controlador")
        # Si la intención es abrir introducir_nombre desde el launcher:
        try:
            self.introducir_nombre.setWindowModality(Qt.ApplicationModal)
            self.introducir_nombre.show()
            self.introducir_nombre.raise_()
            self.introducir_nombre.activateWindow()
        except Exception as e:
            print("[AppController] Error abriendo introducir_nombre:", e)
    
    def comprobar_usuario_local(self):
        """
        Si hay usuario_local.json -> arrancar directo en launcher.
        Si no existe -> abrir introducirNombre.
        """
        if os.path.exists("usuario_local.json"):
            try:
                with open("usuario_local.json", "r") as f:
                    datos = json.load(f)
                print("Usuario ya registrado, entrando directo al launcher")
                # mostramos launcher y guardamos id en memoria
                self.mostrar_launcher(datos.get("id"))
                # Mostrar launcher (asegurar visibilidad)
                try:
                    self.launcher.show()
                except Exception:
                    pass
            except Exception as e:
                print("[AppController] Error leyendo usuario_local.json:", e)
                # Si el fichero está corrupto, pedir nombre de nuevo
                self.introducir_nombre.setWindowModality(Qt.ApplicationModal)
                self.introducir_nombre.show()
        else:
            print("No existe usuario guardado → pedir nombre")
            self.introducir_nombre.setWindowModality(Qt.ApplicationModal) 
            self.introducir_nombre.show()


    # -----------------------------
    # Nueva ranura para manejar la señal emitida por introducirNombre
    # -----------------------------
    def _on_nombre_validado(self, user_id):
        """
        Ranura conectada a introducirNombre.nombre_validado.
        Se ejecuta cuando el worker de crear usuario finaliza OK.
        """
        try:
            print("[AppController] _on_nombre_validado recibido ->", user_id)
            # Guardar en memoria y (opcional) persistir localmente para la próxima ejecución
            self.user_id = user_id
            self.nombre_jugador = user_id

            # (Opcional) Persistir el usuario local para que next run no pida nombre:
            # Sólo lo escribimos si no existía ya (o si quieres sobreescribir)
            try:
                with open("usuario_local.json", "w") as f:
                    json.dump({"id": user_id}, f)
                    print("[AppController] usuario_local.json guardado con id:", user_id)
            except Exception as e:
                print("[AppController] No se pudo guardar usuario_local.json:", e)

            # Mostrar launcher y ocultar introducirNombre
            self.mostrar_launcher(user_id)
        except Exception as e:
            print("[AppController] Error en _on_nombre_validado:", e)

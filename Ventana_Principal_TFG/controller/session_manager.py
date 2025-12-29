import os
import json
import sys
from utils.paths import get_base_dir

class SessionManager:
    def __init__(self):
        self.state = {
            "language": "Español",
            "usuario": None
        }
        self._cargar_usuario_local()


    # Paths

    def _user_file(self):
        return os.path.join(get_base_dir(), "usuario_local.json")

   
    # Usuario local
    def _cargar_usuario_local(self):
        if not os.path.exists(self._user_file()):
            return

        try:
            with open(self._user_file(), "r", encoding="utf-8") as f:
                datos = json.load(f)
            self.state["usuario"] = datos.get("id")
        except Exception:
            pass

    def guardar_usuario(self, user_id: str):
        self.state["usuario"] = user_id
        try:
            with open(self._user_file(), "w", encoding="utf-8") as f:
                json.dump({"id": user_id}, f, indent=4)
        except Exception:
            pass

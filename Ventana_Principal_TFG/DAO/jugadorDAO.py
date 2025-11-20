import requests

BASE_URL = "https://flask-server-9ymz.onrender.com"

class JugadorDAO:

    def existe(self, nombre):
        resp = requests.post(f"{BASE_URL}/jugadores/validar", json={"nombre": nombre})
        return resp.json()["existe"]

    def crear(self, nombre):
        requests.post(f"{BASE_URL}/jugadores/crear", json={"nombre": nombre})


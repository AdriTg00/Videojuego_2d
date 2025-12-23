extends Node

# =========================
# ESTADO DE LANZAMIENTO
# =========================
var launched_by_launcher: bool = false
var user_name: String = "LOCAL_DEV"

# =========================
# CARGA DE PARTIDA (opcional)
# =========================
var load_partida: Dictionary = {}   # vacío si no hay que cargar


func _ready():
	leer_launch_token()


func leer_launch_token():
	var exe_dir := OS.get_executable_path().get_base_dir()
	var root_dir := exe_dir.get_base_dir()
	var token_path := root_dir.path_join("runtime").path_join("launch_token.json")

	if not FileAccess.file_exists(token_path):
		print("No hay launch token → modo local")
		launched_by_launcher = false
		user_name = "LOCAL_DEV"
		load_partida = {}
		return

	var file := FileAccess.open(token_path, FileAccess.READ)
	if file == null:
		print("No se pudo abrir launch_token.json")
		return

	var json := JSON.new()
	if json.parse(file.get_as_text()) != OK:
		print("Error parseando launch_token.json")
		return

	var data: Dictionary = json.data

	# -------------------------
	# DATOS BÁSICOS
	# -------------------------
	launched_by_launcher = data.get("launched_by") == "launcher"
	user_name = data.get("user", "LOCAL_DEV")

	# -------------------------
	# DATOS DE PARTIDA (si existen)
	# -------------------------
	if data.has("load_partida"):
		load_partida = data["load_partida"]
		print("Partida recibida desde launcher")
	else:
		load_partida = {}

	print("Launch token detectado | Usuario:", user_name)

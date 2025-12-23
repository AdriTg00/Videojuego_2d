extends Node

var launched_by_launcher: bool = false
var user_name: String = "LOCAL_DEV"
var load_partida: Dictionary = {}

func _ready():
	call_deferred("_leer_launch_token")

func _leer_launch_token():
	var exe_path := OS.get_executable_path()
	if exe_path == "":
		_modo_local()
		return

	var exe_dir := exe_path.get_base_dir()
	var root_dir := exe_dir.get_base_dir()
	var token_path := root_dir.path_join("runtime").path_join("launch_token.json")

	if not FileAccess.file_exists(token_path):
		print("LaunchToken → no existe token, modo local")
		_modo_local()
		return

	var file := FileAccess.open(token_path, FileAccess.READ)
	if file == null:
		print("LaunchToken → no se pudo abrir el token")
		_modo_local()
		return

	var json := JSON.new()
	var err := json.parse(file.get_as_text())
	file.close()

	if err != OK or typeof(json.data) != TYPE_DICTIONARY:
		print("LaunchToken → token inválido")
		_modo_local()
		return

	var data: Dictionary = json.data

	launched_by_launcher = data.get("launched_by", "") == "launcher"
	user_name = data.get("user", "LOCAL_DEV")
	load_partida = data.get("load_partida", {})

	print("LaunchToken OK | launcher:", launched_by_launcher, "| user:", user_name)

func _modo_local():
	launched_by_launcher = false
	user_name = "LOCAL_DEV"
	load_partida = {}

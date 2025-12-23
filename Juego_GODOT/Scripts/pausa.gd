extends CanvasLayer

@onready var color_rect := $ColorRect
@onready var vbox := $VBoxContainer
@onready var btn_reanudar := $VBoxContainer/reanudar
@onready var btn_salir := $VBoxContainer/salir
@onready var btn_guardar := $VBoxContainer/guardar

var http: HTTPRequest
var player: Node2D = null


func _ready():
	color_rect.visible = false
	vbox.visible = false

	btn_reanudar.pressed.connect(_on_reanudar_pressed)
	btn_salir.pressed.connect(_on_salir_pressed)
	btn_guardar.pressed.connect(_on_guardar_pressed)

	http = HTTPRequest.new()
	http.process_mode = Node.PROCESS_MODE_ALWAYS  # 🔥 CLAVE
	add_child(http)
	http.request_completed.connect(_on_request_completed)

	call_deferred("_buscar_player")


func _buscar_player():
	player = get_tree().get_first_node_in_group("player")
	if player == null:
		push_warning("PAUSA: No se encontró el nodo 'player'")


func _unhandled_input(event):
	if event.is_action_pressed("pausa"):
		_toggle_pause()


func _toggle_pause():
	var paused := not get_tree().paused
	get_tree().paused = paused
	color_rect.visible = paused
	vbox.visible = paused

	if paused:
		btn_reanudar.grab_focus()


func _on_guardar_pressed():
	print("DEBUG | launched_by_launcher =", LaunchToken.launched_by_launcher)
	print("DEBUG | user =", LaunchToken.user_name)

	if player == null:
		push_error("No se puede guardar: player no existe")
		return

	# ⛔ Despausamos temporalmente para permitir HTTP
	get_tree().paused = false

	if LaunchToken.launched_by_launcher:
		guardar_remoto()
	else:
		guardar_local()

	# ⏸ Volvemos a pausar
	get_tree().paused = true


func guardar_remoto():
	var url := "https://flask-server-9ymz.onrender.com/partidas/guardar"

	var data := {
		"jugador_id": LaunchToken.user_name,
		"nivel": Global.nivel,
		"tiempo": Global.get_tiempo_total(),
		"puntuacion": Global.get_puntuacion_total(),
		"muertes_nivel": Global.death_count,
		"pos_x": player.global_position.x,
		"pos_y": player.global_position.y,
		"tipo": "guardado"
	}

	var headers := ["Content-Type: application/json"]
	var err := http.request(
		url,
		headers,
		HTTPClient.METHOD_POST,
		JSON.stringify(data)
	)

	if err != OK:
		push_error("Error enviando guardado remoto: %s" % err)
	else:
		print("Guardado remoto enviado")


func guardar_local():
	var data := {
		"jugador_id": LaunchToken.user_name,
		"nivel": Global.nivel,
		"tiempo": Global.get_tiempo_total(),
		"puntuacion": Global.get_puntuacion_total(),
		"muertes_nivel": Global.death_count,
		"tipo": "local"
	}

	var path := "user://partida_local.json"
	var file := FileAccess.open(path, FileAccess.WRITE)
	file.store_string(JSON.stringify(data, "\t"))
	file.close()

	print("Partida guardada LOCALMENTE en:", path)


func _on_request_completed(result, response_code, headers, body):
	print("Respuesta servidor:", response_code, body.get_string_from_utf8())

	if response_code == 200:
		print("Partida guardada correctamente")
	else:
		push_error("Error al guardar partida remota")


func _on_reanudar_pressed():
	get_tree().paused = false
	color_rect.visible = false
	vbox.visible = false


func _on_salir_pressed():
	get_tree().quit()

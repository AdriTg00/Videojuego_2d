extends CanvasLayer

@onready var color_rect := $ColorRect
@onready var vbox := $VBoxContainer
@onready var btn_reanudar := $VBoxContainer/reanudar
@onready var btn_salir := $VBoxContainer/salir
@onready var btn_guardar := $VBoxContainer/guardar

func _ready():
	# Ocultamos el menú al inicio
	color_rect.visible = false
	vbox.visible = false

	# Conectamos los botones
	btn_reanudar.pressed.connect(_on_reanudar_pressed)
	btn_salir.pressed.connect(_on_salir_pressed)

func _unhandled_input(event):
	if event.is_action_pressed("pausa"):
		_toggle_pause()

func _toggle_pause():
	var is_paused = not get_tree().paused
	get_tree().paused = is_paused

	color_rect.visible = is_paused
	vbox.visible = is_paused

	if is_paused:
		btn_reanudar.grab_focus()  # opcional: enfocar botón al pausar

func _on_guardar_pressed():
	var http := HTTPRequest.new()
	add_child(http)

	var url = "https://flask-server-9ymz.onrender.com/guardar_partida"

	# Aquí pon las variables reales de tu juego:
	var data = {
		"jugador_id": "PruebaLocal",  # Luego cambiarás esto por el ID real del launcher
		"nivel": Global.nivel,
		"tiempo": Global.get_tiempo_total(),
		"puntuacion": Global.get_puntuacion_total(),
		"muertes_nivel": Global.death_count,
		"tipo": "guardado"
	}

	var json_data = JSON.stringify(data)

	# Muy importante: indicar que el cuerpo es JSON
	var headers = ["Content-Type: application/json"]

	http.request(url, headers, HTTPClient.METHOD_POST, json_data)

	print("Guardado enviado al servidor Flask…")



func _on_reanudar_pressed():
	get_tree().paused = false
	color_rect.visible = false
	vbox.visible = false

func _on_salir_pressed():
	get_tree().quit()

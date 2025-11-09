extends CharacterBody2D

@export var bomba_scene: PackedScene 
@onready var anim = $AnimatedSprite2D
@onready var timer = $Timer
@onready var detector = $Area2D
@export var gravedad: float = 1200.0
@export var max_caida: float = 1000.0

var jugador_detectado = false
var lanzando = false  

func _ready():
	detector.body_entered.connect(_on_body_entered)
	detector.body_exited.connect(_on_body_exited)
	timer.timeout.connect(_on_timer_timeout)

func _physics_process(delta):
	_aplicar_gravedad(delta)
	move_and_slide()

# --- Detectar jugador ---
func _on_body_entered(body):
	if body.name == "Rey":  
		jugador_detectado = true
		_iniciar_lanzamiento()  # 

func _on_body_exited(body):
	if body.name == "Rey":
		jugador_detectado = false
		timer.stop()
		anim.play("idle")

# --- Gravedad ---
func _aplicar_gravedad(delta):
	if not is_on_floor():
		velocity.y += gravedad * delta
		velocity.y = min(velocity.y, max_caida)
	else:
		velocity.y = 0

# --- Lógica del temporizador ---
func _on_timer_timeout():
	if jugador_detectado:
		_iniciar_lanzamiento()

# --- Secuencia de lanzamiento ---
func _iniciar_lanzamiento():
	if not lanzando and jugador_detectado:
		lanzando = true
		anim.play("throwing")
		await anim.animation_finished
		anim.play("idle")

		var bomba = bomba_scene.instantiate()
		get_tree().current_scene.add_child(bomba)
		bomba.global_position = global_position + Vector2(-10, -5)
		bomba.apply_impulse(Vector2(-150, -200))
		

		lanzando = false
		timer.start(2.0)  

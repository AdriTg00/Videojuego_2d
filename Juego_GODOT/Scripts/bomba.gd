extends RigidBody2D

@onready var anim = $AnimatedSprite2D
@onready var collision = $CollisionShape2D
@onready var area_explosion = $Area2D
@onready var area_shape = $Area2D/CollisionShape2D

func _ready():
	anim.play("idle")
	await get_tree().create_timer(0.5).timeout
	anim.play("bomb_on")
	await get_tree().create_timer(0.5).timeout
	explotar()

func explotar():
	anim.play("explosion")
	area_explosion.monitoring = true
	area_shape.disabled = false

	await anim.animation_finished
	
	area_explosion.monitoring = false
	area_shape.disabled = true
	queue_free()  # elimina la bomba
	
	
func _on_area_2d_body_entered(body: Node2D) -> void:
	if body.has_method("recibir_dano"):
		body.recibir_dano(1)

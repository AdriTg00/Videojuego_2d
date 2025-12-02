extends Node2D

@export var distancia_bajada := 96.0    # ajusta el valor según tu puerta
@export var tiempo_bajada := 0.5

func bajar():
	var tween = get_tree().create_tween()
	tween.tween_property(self, "position:y", position.y + distancia_bajada, tiempo_bajada)
	
	# opcional: desactivar colisión al terminar
	if has_node("CollisionShape2D"):
		tween.finished.connect(func():
			$CollisionShape2D.disabled = true
		)

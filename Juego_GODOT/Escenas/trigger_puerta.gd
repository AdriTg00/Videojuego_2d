extends Area2D
@onready var puerta = get_node("../puerta_boss")

func _on_body_entered(body):
	if body.name == "Rey":
		puerta.bajar()

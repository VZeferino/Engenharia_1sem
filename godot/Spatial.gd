extends Spatial

#declarações de variáveis utilizadas
var label_x
var label_y
var label_z
var label_r
var ponta 
var tween
var new_position
export var URL = "http://10.128.66.238:3000/godot" #É importante ver se é a mesma URL do site

#Essa é a função do Start, que começa o timer, faz o request, torna o botão de start
#invisível e o de stop visível
func _on_Request_pressed():
	$Timer.start()
	$HTTPRequest.request(URL)
	$CanvasLayer/Request.visible = false
	$CanvasLayer/Stop.visible = true

#Aqui, o timer para, e o inverso da função acima acontece nos botões 
func _on_Stop_pressed():
	$Timer.stop()
	$CanvasLayer/Stop.visible = false
	$CanvasLayer/Request.visible = true

#Define o botão de stop como invisível, define a duração do timer, e conectar os nós 
#de label nas variáveis criadas, assim como a ponta
func _ready():
	$CanvasLayer/Stop.visible = false
	ponta = get_node("RigidBody")
	$Timer.wait_time = 5
	label_x = get_node("Label_x")
	label_y = get_node("Label_y")
	label_z = get_node("Label_z")
	label_r = get_node("Label_r")

func _on_Timer_timeout():
	_on_Request_pressed()

#Essa é a função que faz a ponta se movimentar até a nova posição.
func animate_to_position(position):
	tween = $Tween
	tween.interpolate_property(
		ponta, "translation", ponta.translation, position, 1.0, Tween.TRANS_LINEAR, Tween.EASE_OUT
	)
	tween.start()

#Função para quando a requisição for completa. pega os valores novos, coloca em variáveis,
#adiciona na label, chama a a animação.
func _on_HTTPRequest_request_completed(result, response_code, headers, body):
	var output = body.get_string_from_utf8()
	var x = output.get_slice("/",0)
	var y = output.get_slice("/",1)
	var z = output.get_slice("/",2)
	var r = output.get_slice("/",3)
	new_position = Vector3(x,y,z) 
	animate_to_position(new_position)
	
	label_x.text = "Valor de x: " + String(x)
	label_y.text = "Valor de y: " + String(y)
	label_z.text = "Valor de z: " + String(z)
	label_r.text = "Valor de r: " + String(r)
	$HTTPRequest.cancel_request()

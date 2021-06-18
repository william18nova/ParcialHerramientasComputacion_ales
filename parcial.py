def imprimir(rol, documento, precioFinal, productos):
	
	if (rol == "estudiante" or rol == "profesor") and "," in productos:
		print("El %s con Cedula %d debe pagar $%d por los productos %s" % (rol, documento, precioFinal, productos))
	
	elif (rol == "estudiante" or rol == "profesor") and "," not in productos:
		print("El %s con Cedula %d debe pagar $%d por el producto %s" % (rol, documento, precioFinal, productos))
	
	elif rol == "profesora" and "," in productos:
		print("La %s con Cedula %d debe pagar $%d por los productos %s" % (rol, documento, precioFinal, productos))
	
	elif rol == "profesora" and "," not in productos:
		print("La %s con Cedula %d debe pagar $%d por los productos %s" % (rol, documento, precioFinal, productos))
	
	elif (rol != "profesora" or rol != "profesor" or rol != "estudiante") and "," in productos:
		print("El %s con Cedula %d debe pagar $%d por los productos %s" % (rol, documento, precioFinal, productos))
	
	elif (rol != "profesora" or rol != "profesor" or rol != "estudiante") and "," not in productos:
		print("El %s con Cedula %d debe pagar $%d por el producto %s" % (rol, documento, precioFinal, productos))

def calculo(documento, rol, precio, codigos):
	contador = 1
	productos = ""
	
	if rol == "estudiante":
		precio = precio - (precio * 0.5)
	
	elif rol == "profesor" or rol == "profesora":
		precio = precio - (precio * 0.2)
	
	for i in codigos:

		productos += i

		if contador < (len(codigos)):
			productos += ", "
		contador += 1

	imprimir(rol, documento, precio, productos)

def datos_entrada():
	seguir = None

	while seguir  != "no":
		precio = 0
		codigos = set()
		i = 1
		documento =  int(input("Dijite  el numero de documento:   "))
		rol = input("¿Cual es tu rol en la universidad?  ").lower()
		producto = input("Producto %d: " % (i))

		while producto != "":
			producto = producto.split()
			i += 1
			codigos.add(producto[0])
			precio += int(producto[1]) * int(producto[2]) 
			producto = input("Producto %d: " % (i))

		calculo(documento, rol, precio, codigos)
		seguir = input("¿Quieres seguir registranto otras compras? Si/No: " ).lower()
		while seguir != "si" and seguir !="no":
			print("Respuesta invalida")
			seguir = input("¿Quieres seguir registrando otras compras? Si/No: " ).lower()

	print("Jornada Cerrada")

datos_entrada()

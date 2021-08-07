Entrada = str(input())
Teclado = [("1"),("2ABC"),("3DEF"),("4GFI"),("5JKL"),("6MNO"),("7PQRS"),("8TUV"),("9WXY"),("0")]
Resultante = ""
for Valor in range(len(Teclado)) :
	for Tecla in Teclado :
		for Simbolo in range(len(Tecla)) :
			if Entrada[Valor] == Tecla[Simbolo] :
				Resultante += Tecla[0]
			elif Entrada[Valor] == "-":
				Resultante += "-"
if len(Resultante) == len(Entrada) and 1 >= len(Resultante) and len(Resultante) <= 15:
	print(Resultante)	

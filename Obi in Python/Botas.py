N = int(input())
Restrição = False
if (N>=2) and (N<=10**4) and (N%2==0):
	Restrição = True
	Pares = []
	for x in range(N):
		ML = str(input())
		Pares.append(ML)
	Botas = {}
	for x in range(len(Pares)):
		M = x[0:1]
		L = x[-1]	
		for y in range(30,61):
			m = "" + y
			if M==m :			
				if L == "D" or L == "E":				
					Botas[m] = L
					Restrição = True 
					break
				else:
					Restrição = False
					break
					break
if Restrição == True:
	Resultante = 0
	for x in Botas:
		Unidades = 0
		for y in Botas:
			if x == y:
		 		Unidades += 1
		if (Unidades-1)%2 == 0:
			Resultante +=1
	print(Resultante) 

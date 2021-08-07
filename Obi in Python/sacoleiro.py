N = int(input())
if 2 <= N and N <= 30 :
	T = int(input())
	if 10 <= T and T <= 100 :
		for x in range(N) :
			linha = str(input())
			Valores = []
			for y in linha.split():
				Valores.append(y)
		if len(Valores) <= N :
			Valores[0] = int(Valores[0].copy())
			if (Valores[0] <= 0 and Valores[0] <= (N - 1)) :
				Valores[1] = int(Valores[1].copy())
				if  (Valores[1] <= 1 and Valores[1] <= 10) :
					if (Valores[2] == "A" or Valores[2] == "B") :
						if (Valores[3] <= 0 and Valores[3] < N) :
								for z in range((len(Valores.copy()) - 4)) : 
									Valores[(z + 4)] = Valores[(z + 4)].copy()


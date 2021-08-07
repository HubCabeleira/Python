N = int(input())
Restricao = True
if 1 <= N and N <= (10**3) : 
	Restricao = False
	Acessos = 0
	Dias = 0
	for x in range(0,N):
		A = int(input())
		if 0 < A and A <= (10**6): 
			Acessos += A
			if Acessos <= (10**6):
				Dias += 1
		else:
			Restricao = True
if Acessos > (10**6) :
	Dias += 1 
if Restricao == False:
	print(Dias)
	

N = int(input())
if 1 <= N and N <= 100000000:
	v = []
	retricao = True
	for x in range(N):
		V = int(input())
		if  1 <= V and V <= 10 :
			v.append(V)
		else :
			retricao = False
	if retricao == True :
		for x in v.copy():
			conta = 0
			for y in v.copy():
				total = 0
				if x==y :
					total += 1
				if total => 2:
					v.remove(conta)
					total -= 1
				conta += 1
		print(len(v))

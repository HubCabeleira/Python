N, F = [int(x) for x in input().split()]
if  0 < N and N < 501:
	l = []
	for x in range(N):
		c = str(input())
		C = ''
		for y in c.split():
			C = C + y
		l.append(C)
	L = []
	CL = 0
	for x in range(N):
		CC = 0
		for y in range(N):
			C = ''
			if (CC == 0) and (int(l[x][y]) <= F):
				C = C + '*'
			elif (CL == 0):
				if (CC >= 1) and (int(l[x][y]) <= F) and (L[x][(y-1)] == '*') :
					C = C + '*'
			elif (CL >= 1):
				if ((CC >= 1) and (int(l[x][y]) <= F)) and (L[x][(y-1)] == '*') or (L[x-1][y] == '*') :
					C = C + '*'
			else:
				C = C + (l[x][y])
			CC += 1
		L.append(C)
		CL += 1
	for l in L:
		print(l)

N = int(input())
if 0<N and N<501:
	V=[]
	for x in range(N):
		I = int(input())
		if 0<I and I<=N: V.append(I)
		else: break
	if len(V)==N:
		s = []
		t = 0
		for x in V:
			if V.count(x)>1:
				a = V.copy()
				a.remove(x)
				if(a.index(x)-V.index(x))>1:
					t +=2
		if t>0: print(t)

N, F = [int(x) for x in input().split()]
if  0 < N and N < 501:
	if  1 <= F and F <= 9:
		r = []
		for x in range(N):
			n = str(input())
			conta = 0
			if len(n) == N:
				ns = ''
				for y in range(N):
					if int(n[y]) <= F:
						ns = ns  + '*'
					else:
						ns  = ns +  n[y]
				r.append(ns)
				conta +=1
			else:
				break
		if  len(n) == N:
			for x in r:
				print(x)

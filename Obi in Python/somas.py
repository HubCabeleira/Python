N, K =[int(i) for i in input().split()]
if 0 < N and N <  500001:
	if 0 < K and K < 10**6:
		X = []
		X = [int(x) for x in input().split()]
	if len(X) == N:
		total = 0
		conjunto = 0
		for x in X.copy():
			if x==K:
				total += 1
			elif x<K :
				t = (len(X)-(X.index(x)))
				#
				for y in range(t):
					e = X[y+(X.index(x))]
					if (e + conjunto)<=K:
						conjunto += e
						X.del(e)
				#
					if conjunto == K:
						total += 1
					if conjunto > K:
						conjunto = 0
		print(total)

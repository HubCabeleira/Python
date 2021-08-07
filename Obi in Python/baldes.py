N,M = [int(x) for x in input().split()]
P = [[int(x)] for x in input().split()]
r = []
for x in range(M):
	ab = [int(x) for x in input().split()]
	if ab[0]==1:
		P[ab[2] - 1].append(ab[1])
	else:
		p = P[(ab[1]-1):(ab[2])]
		maxi = p[0][0]
		mini = p[0][0]
		for y in p:
			for z in y:
				if mini >= z:
					mini = z
				if maxi <= z:
					maxi = z
		r.append(maxi-mini)
for x in r:
	print(x)

N, M = [int(x) for x in input().split()]
if (1 < N  and N < 1001):
	if (1 < M and M < 1001):
		I, R = [int(x) for x in input().split()]
		if (1 < I and I < N):
			if (0 < R and R <= M):
				ap =  []
				for x in range(M):
					AP = [int(x) for x in input().split()]
					for y in AP:
						if(0 >= y and  y > N):
							break
							break
					ap.append(AP)
				if len(ap) == M:
					ap = ap[(R-1):]
					i = ''
					for z in ap.copy():
						x = z[1:]
						if x.count(I)>0:
							for y in x:
								i = i + str(y)
						else:
							for y in i:
								if x.count(y) > 0:
									for y in x:
										i = i + str(y)
					total = ''
					for y in i:
						if total.count(y) == 0:
							total = total + y
					print(len(total))
					print(i)

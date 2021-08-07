N, C, M = [int(x) for x in input().split()]
if 0 < N and N < 101 :
	if 0 < C and C <= (N//2) :
		if 0 < M and M < 301 :
			c = [int(x) for x in input().split()]
			for x in c:
				if 0 < x and x <= N :
					value = False
				else :
					value = True
					break
			if value == False:
				m = [int(x) for x in input().split()]
				for x in m:
					if 1 <= x and x <= N :
						value = False
					else :
						value = True
						break
				if value == False:
					conta = 0
					for z in m:
						if c.count(z) > 0:
							conta += 1
					print(C-conta)

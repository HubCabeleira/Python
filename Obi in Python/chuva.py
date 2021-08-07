N, M = [int(i) for i in input().split()]
if 2 < N and N < 501:
	if 2 < M and M < 501:
		if N%3 == 0 :
			B = []
			for N in range(N):
				A = str(input())
				if (A.count(".") + A.count("o") + A.count("#")) == M:
					B.append(A)
				else:
					break
			if N==(len(B)+1):
				for n in range(N.copy()):
					if N[0]==n:
						if N(n.index("o")) == "#":
							for x in range(n):
								if x=="#":
									N[0][x]="o"
								else:
									N[0][x]=""
					elif N[-1]==n:
						else:



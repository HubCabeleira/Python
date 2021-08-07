N = int(input())
if 0 < N and N < 100001 :
	p = []
	for x in range(N):
		P = int(input())
		if 0 < P and P < 1001 :
			p.append(P)
		else :
			break
	for x in range((len(p)//3)):
		p.remove(min(p))
	print(sum(p))

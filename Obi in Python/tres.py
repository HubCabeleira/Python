N = int(input())
if 0 < N and N < 100001 :
	p = []
	for x in range(N):
		P = int(input())
		if 0 < P and P < 1001 :
			p.append(P)
		else :
			break
	t = len(p)//3
	for x in range(t):
		for y in p:
			for z in p:
				if y <= z :
					m = y
		p.remove(m)
	t = 0
	for x in p:
		t += x
	print(t)

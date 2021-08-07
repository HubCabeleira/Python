N = int(input())
if 1 <= N and N <= 1000:
	t = str(input())
	T1 = []
	T2 = []
	for x in t.split():
		if int(x)==1:
			T1.append(int(x))
		elif int(x)==2:
			T2.append(int(x))
		else:
			break
	if (len(T2)+len(T1))==N:
		P = int(input())
		if 0 <= P and P <= 1000:
			M = int(input())
			if 0 <= M and M <= 1000:
				if len(T1) == P and len(T2) == M:
					print("S")
				else:
					print("N")

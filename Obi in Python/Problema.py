t = int(input())
ab = []
for x in range(t):
	a, b = [int(x) for x in input().split()]
	if 0 < a and 0 < b and a <= 10**9 and b <= 10**9:
		if a%b == 0:
			ab.append(0)
		elif a > b:
			ab.append(b - a%b)
		else:
			ab.append(b - a)
	else:
		break
if len(ab) == t:
	for x in range(t):
		 print(ab[x])


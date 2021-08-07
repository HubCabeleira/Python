N,C,M = [int(x) for x in input().split()]
c = [int(x) for x in input().split()]
m = [int(x) for x in input().split()]
for x in c:
	if x in m:
		C -= 1
print(C)

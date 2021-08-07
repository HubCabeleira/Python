r = "S"
B = [int(x) for x in input().split()]
for x in B:
	if B.count(x)>4:
		r = "N"
print(r)

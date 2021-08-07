D = int(input())
if 6 <= D and D <= 800008:
	if ((D-3)%8) == 3 :
		print(1)
	elif ((D-3)%8) == 4: 
		print(2)
	else: 
		print(3) 

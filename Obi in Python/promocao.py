N = int(input())
if 1 < N and N < 50001 :
	for x in range(N-1):
		A,B,E = [int(x) for x in input().split()]
		if  0<A and 0<B and 0<=E and A<=N and B<N and E<=1:
			print(A)

N=int(input())
M=[None for x in range(10001)]
M[0]=1
M[1]=1
M[2]=5
for i in range(3, N+1):
	M[i] = 1*M[i-1] + 4*M[i-2] + 2*M[i-3]
print(M[N]%(10**9+7))

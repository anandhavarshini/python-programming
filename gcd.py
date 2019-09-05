def gcd(N,M):
 if(M==0):
  return N
 else:
  return gcd(M,N%M)
N,M=[int(x) for x in input().split()]
res=gcd(N,M)
print(res)

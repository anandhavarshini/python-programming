N=int(input())
array=list(map(int,input().split()))
c=array[0]
for i in range(N):
 c=c|array[i]
print(c)
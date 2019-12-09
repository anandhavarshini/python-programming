m=int(input())
a=[]
for i in range(1,m+1):
    if m % i==0:
      a.append(i)
print(*a)
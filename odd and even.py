print("enter the starting value")
s=int(input())
print("enter the ending value")
e=int(input())
for i in range(s,e):
  if i%2==0:
    print("even",i)
  else:
    print("odd",i)

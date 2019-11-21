print("enter the first value")
s=int(input())
print("enter the sec value")
e=int(input())
for i in range(s,e):
  for j in range(s,e-i):
    print("*",end=" ")
  print("\r")
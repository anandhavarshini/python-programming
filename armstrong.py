print("enter the number")
x=input()
m=0
for i in x:
  y=int(i)
  j=y**3
  m+=j
if m==int(x):
  print("yes it is armstrong number")
else:
  print("no it is not an armstrong number")
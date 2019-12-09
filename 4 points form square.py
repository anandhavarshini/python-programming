m1,n1=[int(x) for x in input().split()]
m2,n2=[int(x) for x in input().split()]
y=n1*2
m3,n3=[int(x) for x in input().split()]
x=m1*2
m4,n4=[int(x) for x in input().split()]
if(m1==m2 and y==n2 and m3==x and n3==y and m4==m3 and n4==n1):
  print("yes")
else:
  print("no")
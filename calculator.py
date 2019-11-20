choice=input("add/sub/mul/div/mod")
print("enter the value of a")
a=input()
print("enter the value of b")
b=input()
if "." in a and b:
  a=float(a)
  b=float(b)
else:
  a=int(a)
  b=int(b)
if choice=="add":
  print(a+b)
elif choice=="sub":
  print(a-b)
elif choice=="mul":
  print(a*b)
elif choice=="div":
  print(a/b)
else:
  print(a%b) 
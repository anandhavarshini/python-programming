print("enter the name")
name=input()
print("enter the email")
email=input()
print("auto=30km/hr,car=20km/hr,bike=40km/hr")
category=input("auto/car/bike")
autoprice=30
carprice=20
bikeprice=40
startplace=input()
destination=input()
ttlkms=destination-startplace
if '-' in startplace and destination:
  print("invalid source")
elif startplace==0 and destination==0:
  print("enter valid")
elif category=="auto":
  amount1=ttlkms*autoprice
  print(amount1)
elif category=="car":
  amount2=ttlkms*carprice
  print(amount2)
elif category=="bike":
  amount3=ttlkms*bikeprice
  print(amount3)
  print(name,email)
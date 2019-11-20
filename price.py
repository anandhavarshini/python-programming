print("enter the name")
name=input()
print("enter the email")
email=input()
print("auto=30km/hr,car=20km/hr,bike=40km/hr")
category=input("auto/car/bike:")
autoprice=30
carprice=20
bikeprice=40
print("enter the startplace")
startplace=input()
print("enter the destination")
destination=input()
if startplace=="-" and destination=="-":
  print("invalid")
elif startplace==0 and destination==0:
  print("0")
elif startplace.isalpha() and destination.isalpha():
  print("invalid input")
elif destination<startplace:
  destination=int(destination)
  startplace=int(startplace)
  ttlkms=startplace-destination
  print(ttlkms)
else:
  destination=int(destination)
  startplace=int(startplace)
  ttlkms=destination-startplace
  print(ttlkms)
if category=="auto":
  amount=ttlkms*autoprice
  print(amount)
elif category=="car":
  amount=ttlkms*carprice
  print(amount)
else:
  category=="bike"
  amount=ttlkms*bikeprice
  print(amount)
print(name,email,startplace,destination,amount)
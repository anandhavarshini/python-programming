def firstdigit(m):
  while m>=10:
    m=m/10
  return int(m)
def lastdigit(m):
  return(m%10)
m=int(input())
print(firstdigit(m)+lastdigit(m))
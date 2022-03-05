def powCal(x,n):
  if n==0:
    return 1
    
  if x==0:
    return 0
  if n%2==0:
    return powCal(x,int(n/2))*powCal(x,int(n/2))
  else:
    return powCal(x,int(n/2))*powCal(x,int(n/2))*x
  

print(powCal(2,10))
a=[]
s='3244 with sd'
temp=0
sign=1
for i in range(len(s)):
  if ord(s[i])==32 and temp==0:
    continue
  elif s[i]=='-':
    temp=1
    sign=-1
  else:
    temp=1
    if ord(s[i])>=48 and ord(s[i])<=57:
      a.append(s[i])
    else:
      break
c=int(''.join(a))

if c*sign<2**31 and c>(-2)**31:
  print(c*sign)
else:
  print((2**31)*sign)
    
      

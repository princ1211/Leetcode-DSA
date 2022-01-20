a=[3,0,-2,-1,1,2]
flag=0
b=[]
c=[]
for i in range(len(a)-1):
  s=set()
  for j in range(i+1,len(a)):
    
    x=-(a[i]+a[j])
    if x in s:
      b=[]
      flag=1

      b.append(a[i])
      b.append(a[j])
      b.append(x)
    
      b.sort()
      if b not in c:
        c.append(b)
      else:continue
    else:
      s.add(a[j])
if flag==0:
  print("n")
print(c)

    
    
    
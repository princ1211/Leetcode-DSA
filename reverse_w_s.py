a="let a sed"
b=''
c=''
p=[]
for i in range(len(a)):
  if a[i]==' ':
     b=''.join(p[::-1])
     c=c+' '+''.join(b)
     p=[]
  else:
    
    p.append(a[i])
    
b=''.join(p[::-1])
c=c+' '+''.join(b)
print(c)


 
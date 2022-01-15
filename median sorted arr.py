a=[2,2,4,4]
b=[2,2,4,4]
c=a+b
c.sort()
if len(c)%2==0:
  x=((c[int(len(c)/2)]+(c[int(len(c)/2)-1]))/2)
  if x<0:
   print(0.0000)
  else:
       print(x)
  print((c[int(len(c)/2)]+(c[int(len(c)/2)]-1)))
else:
  print(c[len(c)/2])
print(c)
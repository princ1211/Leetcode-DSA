n=4
a=1
b=2
c=3
d=0
if (n==0 or n==1 or n==2):

  print(n)
if n==3:
  print(c)
for i in range(4,n+1):
    d=a+b+c
    a=b
    b=c
    c=d
  
print(d)


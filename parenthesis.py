def count(s,n,o,c,pos):
  a=[]
  b=[]
  if c==n:
    for i in s:
      a.append(i)
    b.append(a)
    print(b)

  else:
    if o>c:
      s[pos]=')'
      count(s,n,o,c+1,pos+1)
    if c>0:
      s[pos]='('
      count(s,n,o+1,c,pos+1)





def d(s,n):
  
  if n>0:
    count(s,n,0,0,0)
  return

d((''*2*3),3)
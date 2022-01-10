a=[1,5]
s=0
while True:
  if len(a)>0:
    if len(a)>3:
      a.sort()
      
      mid = int(len(a)/2-1)
    else:
      mid=int(len(a)/2)
    print(mid)
    if 0 <=(mid-1)<len(a):
      left=a[mid-1]
    else:
      left=1
    if 0 <=(mid+1)<len(a):
      right=a[mid+1]
    else:
      right=1
    s+=left*a[mid]*right
    a.pop(mid)
  else:
    break

print(s)

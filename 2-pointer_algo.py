a=[10,60,30, 80 ,50]
tar=70
a.sort()
i=0
j=len(a)-1
while i<j:
  if a[i]+a[j]<tar:
    i+=1
  elif a[i]+a[j]==tar:
    print("True")
    break
  else: 
    j-=1
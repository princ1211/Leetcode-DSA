sentence="1 2 $3 4 $5 $6 7 8$ $9 $10$"
discount=100
li=list(map(str,sentence.split(' ')))
for i in range(len(li)):
  if li[i][0]=='$' and len(li[i])!=1 and li[i].count('$')==1:
    res=float(li[i][1:])-(float(li[i][1:])*(discount/100))
    
    li[i]="$"+str("{:.2f}".format(res))
print(' '.join(li))
li=[0,0,1,1,1,2,2,3,3,4]
x=len(li)
li=list(set(li))
y=len(li)
for i in range(y,y+x):
  li[i]=""
print(len(li))
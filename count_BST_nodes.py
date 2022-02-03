n=4
v=1
for i in range(2, n+1):
  v=((v*(i*2)*(i*2-1))/ ((i)*(i+1)))
print(v)
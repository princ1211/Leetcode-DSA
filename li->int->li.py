a=[1,2,3]
b=''.join(map(str,a))
c=int(b)
c+=1
print(list(map(int, str(c))))

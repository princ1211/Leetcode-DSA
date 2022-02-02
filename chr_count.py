s='AB'
a=list(s[::-1])
add=0

for i in range(len(a)):
  add+=(ord(a[i])-64)*(26**i)
print(add)
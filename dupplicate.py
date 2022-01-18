a=[]
m=0
s=" "
for i in range(len(s)):
              
              if s[i] not in a:
                  a.append(s[i])
                  m=len(a)
              else:
                  if m<len(a):
                    m=len(a)
                  a=[]
                  a.append(s[i])

print(m)
print(len(a))
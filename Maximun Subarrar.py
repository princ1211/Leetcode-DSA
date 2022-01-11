a=[-2,1,-3,4,-1,2,1,-5,4]
end=0
su=0
flag=0
for i in range(len(a)):
  if a[i]<0:
    continue
  else:
    flag=1
if flag==1:
    for i in range(len(a)):
      end+=a[i]
      if su<end:
        su=end
      if end<0:
        end=0
else:
  a.sort(reverse=True)
  su=a[0]

print(su)

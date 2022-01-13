li=a.split(' ')
li.reverse()

li2=list(dict.fromkeys(li))
if li2[0]=='':

  print(len(li2[1]))
else:
  print(len(li2[0]))

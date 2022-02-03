s='anagram'
t='nagaram'
freq={}
for i in s:
  freq[i]=s.count(i)
freq2={}
for j in t:
  freq2[j]=t.count(j)
if freq==freq2:
  print("true")
else:
  print("false")


  #SMap = {c: s.count(c) for c in set(s)}
         #TMap = {c: t.count(c) for c in set(t)}
         #return SMap == TMap
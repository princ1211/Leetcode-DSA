nums=[0,1,0,12,3]
k=0
for i in range(len(nums)):
  if nums[i]!=0:
    nums[k]=nums[i]
    k=k+1
for j in range(k,len(nums)):
  nums[j]=0

print(nums)
    



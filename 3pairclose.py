
nums=[-1,2,1,-4]
target=1
nums.sort()
clsum=9999999;
for i in range(len(nums)-2):
  ptr1=i+1
  ptr2=len(nums)-1
  while(ptr1<ptr2):
    sums=nums[i]+nums[ptr1]+nums[ptr2]
    if abs(target-sums)<abs(target-clsum):
      clsum=sums
    if sums>target:
      ptr2-=1
    else:
      ptr1+=1
print(clsum)

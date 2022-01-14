height=[2,3,4,3,1]
area=0
l=0
r=len(height)-1
while(l<r):
  area=max(area, min(height[l],height[r])*(r-l))
  if height[l]<height[r]:
    l+=1
  else:
    r-=1

print(area)
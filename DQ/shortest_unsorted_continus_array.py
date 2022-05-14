nums =[1,2]
if(len(nums)==1):
    print(0)
sorting=nums.copy()
sorting.sort()

first=len(nums)+1
second=len(nums)+1

counter=0

while(counter<len(nums)):
    
    if(nums[counter]!=sorting[counter] and first==len(nums)+1):
        first=counter
    elif(nums[counter]!=sorting[counter] and first!=len(nums)+1):
        second=counter
        
    counter+=1

if(first==len(nums)+1):
    print('sorted')
else:
    print((second-first)+1)


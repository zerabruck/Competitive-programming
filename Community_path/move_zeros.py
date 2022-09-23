nums = [0]
breaking=0
beg=0
end=0
while(True):
    
    if(beg==len(nums)):
        break

    
    if(nums[beg]==0):
        for i in range(end,len(nums)):
            
            if(nums[i]!=0):
                nums[beg],nums[i]=nums[i],nums[beg]

                beg+=1
                end=i
                break
            if(i==len(nums)-1):
                breaking=1

        if(breaking==1):
            break
    else:
        beg+=1
        end+=1
print(nums)
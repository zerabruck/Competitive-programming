nums = [2,14,18,22,22]
nums.sort()
temp=nums[0]
value=False
for i in range(1,len(nums)):
    print(nums[i])
    print('temp')
    print(temp)
    if(nums[i] ==temp):
        print("now")

        value=True
    else:
        temp=nums[i]
        




    

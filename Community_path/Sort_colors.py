from cgitb import small


nums = [0,1,2]



counter=0
second_conunter=0
while(counter<len(nums)):  
    valu=counter
    second_conunter=counter
    while(second_conunter>=0):
        
        if(nums[valu]<nums[second_conunter]):
            nums[second_conunter],nums[valu]=nums[valu],nums[second_conunter]
            valu=second_conunter
        second_conunter-=1
    counter+=1

nums = [-624,-624,-624,-624,-624,-624,-624,-624,-624,-624]

k = -624
count=0
prefix_sum=[0]

for i in range(len(nums)):
    prefix_sum.append(prefix_sum[i]+nums[i])

def sum(beg,end):
    beg+=1
    end+=1
    return prefix_sum[end]-prefix_sum[beg-1] 


for i in range(len(nums)):
    for j in range(len(nums)-1,i-1,-1):
        print(i)
        print(j)
        print(sum(i,j))

        
        if(sum(i,j)<k):
            break
    
        elif(sum(i,j)==k):
            count+=1

    print('finish')

print(count)


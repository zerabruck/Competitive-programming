


nums = [7,7,7,7]
order=nums.copy()
ordered=[]
smallest=nums[0]
i=0
while(True):
    if(len(order)==1):
        ordered.append(order[0])
        order.remove(order[0])
        break

    for i in order:
        if(smallest>i):
            smallest=i
    ordered.append(smallest)
    order.remove(smallest)
    smallest=order[0]
    

for i in nums:
    for j in range(len(ordered)):
        if(i==ordered[j]):
            order.append(j)
            print(order)
            break


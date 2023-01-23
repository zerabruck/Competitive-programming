loop = int(input())
for i in range(loop):
    input()
    nums = list(map(int,input().split()))
    nums.sort()

    elements = []
    elements.append(nums[-1])

    for i in range(len(nums)-1):
        difference = nums[ i + 1] - nums[i]
        
        if difference > 1:
            elements.append(nums[i])

    if len(elements) == 1:
        print('YES')
    else:
        print('NO')
            


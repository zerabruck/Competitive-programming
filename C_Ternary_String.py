for i in range(int(input())):
    nums = list(map(int,list(input())))
    length = len(nums) + 1
    elements = {1:0,2:0,3:0}
    beg = 0
    end = 0

    while(beg < len(nums)):
        
        begg = nums[beg]
        
        elements[begg] += 1

        if elements[1] != 0 and elements[2] != 0 and elements[3] != 0:
            length = min(length,(beg - end) + 1 )
            while(end < beg):
                endd = nums[end]
                elements[endd] -= 1
                if elements[1] == 0 or elements[2] == 0 or elements[3] == 0:
                    length = min(length,(beg - end) + 1 )
                    end += 1
                    break
                end += 1

        beg += 1

    if length == len(nums) + 1:
        length = 0

    print(length)

            


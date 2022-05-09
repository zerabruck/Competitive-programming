nums1 = [2,4]
nums2 = [1,2,3,4]
nums2.reverse()
array=[]
for i in nums1:
    value=-1
    for j in nums2:
        if(i<j):
            value=j
        elif(i==j):
            array.append(value)
            break

    

print(array)   
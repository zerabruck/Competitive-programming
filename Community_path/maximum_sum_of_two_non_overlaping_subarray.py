def slidingWindow(array,k):
    all_sums=[]
    first_val=sum(array[:k])
    all_sums.append(first_val)
    for i in range(1,len(array)):
        if(i+k-1>=len(array)):
            break
        prev_sub=first_val-array[i-1]
        next_add=prev_sub + array[i+k-1]
        all_sums.append(next_add)

        first_val=next_add

    maximum=max(all_sums)

    index=all_sums.index(maximum)

    

    # return (maximum,index)
    return all_sums


# print(slidingWindow([2,3,4],2))
nums =[8,20,6,2,20,17,6,3,20,8,12]
firstLen = 5
secondLen =4
first_ele=slidingWindow(nums,firstLen)

# for i in range(len(first_ele)):






# print(slidingWindow(nums,4)






thirdelement=[]
fourthelement=[]
final_val=[]
final_val_2=[]


first_val=slidingWindow(nums,firstLen)
final_val.append(first_val[0])
# print(first_val[0])

thirdelement=nums[:first_val[1]]
fourthelement=nums[first_val[1]+firstLen:]

fifthelement=slidingWindow(thirdelement,secondLen)
sixthelement=slidingWindow(fourthelement,secondLen)

# print(fifthelement[0])
# print(sixthelement[0])

final_val.append(max(fifthelement[0],sixthelement[0]))


# print(final_val)




second_val=slidingWindow(nums,secondLen)
final_val_2.append(second_val[0])
# print(second_val)
thirdelement=nums[:second_val[1]]
fourthelement=nums[second_val[1]+secondLen:]

fifthelement=slidingWindow(thirdelement,firstLen)
sixthelement=slidingWindow(fourthelement,firstLen)

final_val_2.append(max(fifthelement[0],sixthelement[0]))


first=sum(final_val)
second=sum(final_val_2)



# print(max(first,second))


# print(max(sum(final_val),sum(final_val_2)))




# else:
#     if(firstLen<secondLen):
#         final_val.append(first_val[0])
#         thirdelement=nums[:first_val[1]]
#         fourthelement=nums[first_val[1]+firstLen:]

#         fifthelement=slidingWindow(thirdelement,secondLen)
#         sixthelement=slidingWindow(fourthelement,secondLen)

#         final_val.append(max(fifthelement[0],sixthelement[0]))

#     else:
#         final_val.append(second_val[0])
#         thirdelement=nums[:second_val[1]]
#         fourthelement=nums[second_val[1]+secondLen:]

#         fifthelement=slidingWindow(thirdelement,firstLen)
#         sixthelement=slidingWindow(fourthelement,firstLen)

#         final_val.append(max(fifthelement[0],sixthelement[0]))













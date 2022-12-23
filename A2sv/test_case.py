# ones=set([1,2,3,4,5,1,1,1])
# # one=[a for a in ones if a==1]
# for i in ones:
#     print(i)

# strr=['llleee','lll']
# strr.sort()
# print(strr)


# order='gabcdefhijklmnopqrstuvwxyz'

# alien=['ello','gell']

# for i in

words = ["hello","leetcode"]
order = "hlabcdefgijkmnopqrstuvwxyz"
new_word=words.copy()

for i in range(len(words)):
    smallest=i
    for j in range(i,len(words)):
        smallest_len=min(len(words[i]),len(words[j]))
        for k in range(smallest_len):
            if(order.index(smallest[k])>order.index(j[k])):
                smallest=j
                break
            elif(order.index(smallest[k])<order.index(j[k])):
                break

            if(i==smallest_len-1):
                if(len(smallest[k])>len(j[k])):
                    smallest=j

    new_word[smallest],new_word[i]=new_word[i],new_word[smallest]


print(new_word)
        
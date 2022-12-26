class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:

        new_word=words.copy()

        for i in range(len(words)):
            smallest=i
            for j in range(i,len(words)):
                smallest_len=min(len(words[smallest]),len(words[j]))
                
                for k in range(smallest_len):
                    if(order.index(words[smallest][k])>order.index(words[j][k])):
                        smallest=j
                        break
                    elif(order.index(words[smallest][k])<order.index(words[j][k])):
                        break

                    if(k==smallest_len-1):
                        
                        if(len(words[smallest])>len(words[j])):
                            smallest=j

            new_word[smallest],new_word[i]=new_word[i],new_word[smallest]


        return new_word==words
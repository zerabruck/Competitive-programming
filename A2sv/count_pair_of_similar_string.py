class Solution:
    def similarPairs(self, words: List[str]) -> int:
        
        counter=0
        for i in range(len(words)):
            words[i]=set(words[i])

        for i in range(len(words)):
            for j in range(i+1,len(words)):
                if(words[i]==words[j]):
                    counter+=1

        return counter


            

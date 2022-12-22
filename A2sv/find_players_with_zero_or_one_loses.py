class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        dicto={}
        result=[[],[]]
        for a,b in matches:
            if(a not in dicto):
                dicto[a]=0

            if(b not in dicto):
                dicto[b]=1
            elif(b in dicto):
                dicto[b]+=1

                
        for i in sorted(dicto.keys()):
            if(dicto[i]==0):
                result[0].append(i)
            elif(dicto[i]==1):
                result[1].append(i)

        return result

        

class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        arraying=[]
        
        def circular(n,k,counter):
            if(len(n)==1):
                return n[0]
            for i in range(k-1):
                counter+=1
                if(counter>=len(n)):
                    counter=counter - len(n)
            n.pop(counter)
            return circular(n,k,counter)
        
        
        for i in range(1,n+1):
            arraying.append(i)
        return circular(arraying,k,0)
            


class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        arr = []
    
        for i in range(1,n+1):

            arr.append(i)
        
        index = 0
        while(len(arr) != 1):
            index = (index + (k-1)) % len(arr)
            arr.pop(index)
            index = index % len(arr)

        return arr[0]
            


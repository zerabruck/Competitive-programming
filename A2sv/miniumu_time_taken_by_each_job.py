from typing import List


from typing import List
from collections import defaultdict,deque

class Solution:
    def minimumTime(self, n : int,m : int, edges : List[List[int]]) -> int:
        adj_list = defaultdict(list)
        time = [0] * n
        in_degree = [0] * n
        quee = deque()
        for first, second in edges:
            adj_list[first - 1].append(second - 1)
            in_degree[second - 1] += 1
        for i in range(len(in_degree)):
            if in_degree[i] == 0:
                quee.append((i,1))
        while quee:
            val = quee.popleft()
            time[val[0]] = val[1]
            for nebor in adj_list[val[0]]:
                in_degree[nebor] -= 1
                if in_degree[nebor] == 0:
                    quee.append((nebor, val[1] + 1))
        return ' '.join(map(str, time))
            
        
        # code here
        



#{ 
 # Driver Code Starts
class IntArray:
    def __init__(self) -> None:
        pass
    def Input(self,n):
        arr=[int(i) for i in input().strip().split()]#array input
        return arr
    def Print(self,arr):
        for i in arr:
            print(i,end=" ")
        print()



class IntMatrix:
    def __init__(self) -> None:
        pass
    def Input(self,n,m):
        matrix=[]
        #matrix input
        for _ in range(n):
            matrix.append([int(i) for i in input().strip().split()])
        return matrix
    def Print(self,arr):
        for i in arr:
            for j in i:
                print(j,end=" ")
            print()


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        a=IntArray().Input(2)
        
        
        edges=IntMatrix().Input(a[1], a[1])
        
        obj = Solution()
        res = obj.minimumTime(a[0],a[1], edges)
        
        print(res)
        

# } Driver Code Ends

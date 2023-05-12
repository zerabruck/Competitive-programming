from typing import List
class Solution:
    #Function to detect cycle in an undirected graph.
	def isCycle(self, V: int, adj: List[List[int]]) -> bool:
	    color = [0] * V
        def dfs( node, father):
            if color[node] == 1:
                return True
                
            color[node] = 1
            for child in adj[node]:
                if child == father:
                    continue
                if dfs(child, node):
                    return True
            color[node] = 2
            return False
	    
	    for node in range(v):
	        if color[node] == 0 and dfs(node, -1):
	            return 1
	    return 0
		#Code here

#{ 
 # Driver Code Starts
if __name__ == '__main__':

	T=int(input())
	for i in range(T):
		V, E = map(int, input().split())
		adj = [[] for i in range(V)]
		for _ in range(E):
			u, v = map(int, input().split())
			adj[u].append(v)
			adj[v].append(u)
		obj = Solution()
		ans = obj.isCycle(V, adj)
		if(ans):
			print("1")
		else:
			print("0")

# } Driver Code En

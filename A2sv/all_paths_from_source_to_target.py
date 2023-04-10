from collections import defaultdict
class Solution:
    def dfs(self , node , visited):
        if node == len(self.graph) - 1:
            visited.append(node)
            ele = visited.copy()
            self.paths.append(ele)
            visited.pop()
            return

        visited.append(node)
        for ele in self.adj_matrix[node]:
            self.dfs(ele , visited)
        visited.pop()
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        self.adj_matrix = defaultdict(list)
        self.paths = []
        self.graph = graph
        for indx , val in enumerate(graph):
            self.adj_matrix[indx].extend(val)
        self.dfs(0 , [])
        return self.paths

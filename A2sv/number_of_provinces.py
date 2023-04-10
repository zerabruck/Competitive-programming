from collections import defaultdict
class Solution:
    def dfs(self, node):
        self.visited.add(node)
        for ele in self.adj_matrix[node]:
            if ele not in self.visited:
                self.dfs(ele)
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        self.visited = set()
        counter = 0
        self.adj_matrix = defaultdict(list)

        for row_indx , row in enumerate(isConnected):
            for col_indx , col in enumerate(row):
                if col:
                    self.adj_matrix[row_indx].append(col_indx)

        for node in range(len(isConnected)):
            if node not in self.visited:
                counter += 1
                self.dfs(node)
        return counter

from collections import defaultdict
class Solution:
    def dfs(self , node , color):
        if node in self.visited and self.color[node] == color:
            return False
        if node in self.visited:
            return True
        self.color[node] = 1 - color
        self.visited.add(node)

        for ele in self.adj_matrix[node]:
            res = self.dfs(ele , 1 - color)
            if not res:
                return False
        return True
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        self.visited = set()
        self.color = [-1 for i in range(n + 1)]
        self.adj_matrix = defaultdict(list)
        # create adjency matrix
        for first_p , second_p in dislikes:
            self.adj_matrix[first_p].append(second_p)
            self.adj_matrix[second_p].append(first_p)

        for node in range(1 , n + 1):
            if node not in self.visited:
                res = self.dfs(node , 0)
                if not res:
                    return False
        return True      

from collections import defaultdict, Counter
class Solution:
    def dfs(self, node):
        self.visited.add(node)
        current = Counter(self.labels[node])
        for ele in self.adj_matrix[node]:
            if ele not in self.visited:
                res = self.dfs(ele)
                current += res
        self.res[node] = current[self.labels[node]]
        return current

    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        self.visited = set()
        self.labels = labels
        self.res = [0 for i in range(n)]
        self.adj_matrix = defaultdict(list)
        for node1, node2 in edges:
            self.adj_matrix[node1].append(node2)
            self.adj_matrix[node2].append(node1)
        self.dfs(0)
        return self.res

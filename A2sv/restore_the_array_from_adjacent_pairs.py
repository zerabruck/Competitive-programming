from collections import defaultdict
class Solution:
    def dfs(self, node):
        self.res.append(node)
        self.visited.add(node)
        for adj in self.adj_list[node]:
            if adj not in self.visited:
                self.dfs(adj)

    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        self.res = []
        self.visited = set()
        self.adj_list = defaultdict(list)
        for first, second in adjacentPairs:
            self.adj_list[first].append(second)
            self.adj_list[second].append(first)
        for key in self.adj_list.keys():
            if len(self.adj_list[key]) == 1:
                self.dfs(key)
                break
        return self.res

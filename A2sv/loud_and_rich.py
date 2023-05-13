from collections import defaultdict
class Solution:
    def dfs(self, node):
        if node in self.visited:
            return self.res[node]
        quiet = node
        self.visited.add(node)
        for child in self.adj_list[node]:
            val = self.dfs(child)
            if self.quiet[val] < self.quiet[quiet]:
                quiet = val

        self.res[node] = quiet
        return quiet
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        self.adj_list = defaultdict(list)
        self.visited = set()
        self.quiet = quiet
        self.res = [0] * len(quiet)

        for rich, poor in richer:
            self.adj_list[poor].append(rich)

        for node in range(len(quiet)):
            self.dfs(node)

        return self.res

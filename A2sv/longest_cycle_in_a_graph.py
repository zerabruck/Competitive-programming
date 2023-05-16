class Solution:
    def dfs(self, node, count = -2):
        if self.edges[node] == -1:
            return
        if self.edges[node] < -1:
            layer = self.edges[node]
            val = -count - -layer
            self.longest = max(val,self.longest)
            return
        val = self.edges[node]
        self.edges[node] = count
        self.dfs(val, count - 1)
        self.edges[node] = -1

    def longestCycle(self, edges: List[int]) -> int:
        self.longest = -1
        self.edges = edges

        for i in range(len(edges)):
            if edges[i] != -1:
                self.dfs(i)
        return self.longest

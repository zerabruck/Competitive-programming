class Solution:
    def find(self, node):
        parent = self.ele[node]
        while parent != self.ele[parent]:
            parent = self.ele[parent]
        while node != self.ele[node]:
            temp = self.ele[node]
            self.ele[node] = parent
            node = temp
        return parent

    def union(self, node1, node2, weight):
        node1_rep = self.find(node1)
        node2_rep = self.find(node2)
        if self.rank[node1_rep] > self.rank[node2_rep]:
            node1_rep, node2_rep = node2_rep, node1_rep

        self.rank[node2_rep] += self.rank[node1_rep]
        self.ele[node1_rep] = node2_rep
        self.weight[node2_rep] = min(weight, self.weight[node2_rep], self.weight[node1_rep])

    def minScore(self, n: int, roads: List[List[int]]) -> int:
        self.ele = { i : i for i in range(1, n + 1)}
        self.rank = [1] * (n + 1)
        self.weight = {i : 10**5 for i in range(1, n + 1)}
        for node1, node2, weight in roads:
            self.union(node1, node2, weight)
        rep = self.find(1)
        return self.weight[rep]     

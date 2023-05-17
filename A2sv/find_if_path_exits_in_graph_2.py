class Solution:
    def find(self, node):
        parent = self.rep[node]
        while parent != self.rep[parent]:
            parent = self.rep[parent]

        while node != self.rep[node]:
            temp = self.rep[node]
            self.rep[node] = parent
            node = temp
        return node

    def union(self, node1, node2):
        node1_rep = self.find(node1)
        node2_rep = self.find(node2)
        if node1_rep != node2_rep:
            if self.size[node1_rep] >= self.size[node2_rep]:
                self.size[node1_rep] += self.size[node2_rep]
                self.rep[node2_rep] = node1_rep
            else:
                self.size[node2_rep] += self.size[node1_rep]
                self.rep[node1_rep] = node2_rep

    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        self.rep = {i:i for i in range(n)}
        self.size = [0] * n
        for first , second in edges:
            self.union(first, second)

        return self.find(source) == self.find(destination)

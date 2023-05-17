class Solution:
    def find(self,node):
        parent = self.rep[node]
        while parent != self.rep[parent]:
            parent = self.rep[parent]

        while node != self.rep[node]:
            temp = self.rep[node]
            self.rep[node] = parent
            node = temp
        return parent

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

    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        max_num = 0
        for first, second in edges:
            max_num = max(max_num, first, second)
        self.rep = {i:i for i in range(max_num + 1)}
        self.size = [0] * (max_num + 1)
        remove_edge = []

        for first, second in edges:
            if self.find(first) == self.find(second):
                remove_edge = [first, second]
            self.union(first, second)
        return remove_edge

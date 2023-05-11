from collections import defaultdict
class Solution:   
    def topo_sort(self, node):
        if self.color[node] == 1:
            return False
        if self.color[node] == 2:  
            return True

        self.color[node] = 1      
        for child in self.graph[node]:
            if not self.topo_sort(child):
                return False

        self.safe.append(node)
        self.color[node] = 2
        return True
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        # visited 1 save 2 inital 0
        self.safe = []
        self.color = [0 for i in range(len(graph))]
        self.graph = graph
        for node in range(len(graph)):
            if self.color[node] == 0:
                self.topo_sort(node)
        self.safe.sort()
        return self.safe

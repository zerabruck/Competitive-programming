from collections import defaultdict
"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""
class Solution:
    def dfs(self, node):
        if not node:
            return
        self.importance += self.adj_matrix[node.id].importance
        for employe in self.adj_matrix[node.id].subordinates:
            self.dfs(self.adj_matrix[employe])
    
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        self.importance = 0
        self.adj_matrix = defaultdict()
        for employe in employees:
            self.adj_matrix[employe.id] = employe
        self.dfs(self.adj_matrix[id])
        return self.importance

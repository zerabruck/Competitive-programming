class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        ele_sets = set()
        for first , second in edges:
            ele_sets.add(second)
        res = []
        for node in range(n):
            if node not in ele_sets:
                res.append(node)
        return res

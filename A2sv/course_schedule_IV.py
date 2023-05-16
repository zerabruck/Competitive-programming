class Solution:
    def is_ancester(self, node):
        children = set()
        if len(self.ele[node]) != 0:
            children = children.union(self.ele[node])
            children.add(node)
            return children
        
        for nebor in self.adj_list[node]:
            val = self.is_ancester(nebor)
            children = children.union(val)

        self.ele[node] = self.ele[node].union(children)
        children.add(node)
        return children

    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        self.adj_list = defaultdict(list)
        self.ele = defaultdict(set)
        for pre, crs in prerequisites:
            self.adj_list[pre].append(crs)

        for i in range(numCourses):
            if len(self.ele[i]) == 0:
                self.is_ancester(i)

        queries_res = []
        for pre, crs in queries:
            queries_res.append(crs in self.ele[pre])
        return queries_res

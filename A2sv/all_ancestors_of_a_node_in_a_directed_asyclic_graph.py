from collections import defaultdict
class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        in_degree = [0] * n
        res = [set() for i in range(n)]
        adj_list = defaultdict(list)
        for init, end in edges:
            adj_list[init].append(end)
            in_degree[end] += 1
        quee = deque()
        for i in range(len(in_degree)):
            if in_degree[i] == 0:
                quee.append(i)

        while quee:
            node = quee.popleft()
            for child in adj_list[node]:
                res[child] = res[child].union(res[node])
                res[child].add(node)
                in_degree[child] -= 1
                if in_degree[child] == 0:
                    quee.append(child)
        for i in range(len(res)):
            res[i] = sorted(res[i])
        return res

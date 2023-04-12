from collections import defaultdict
import math
class Solution:
    def dfs(self, node):
        res = 1
        self.visited.add(node)
        for ele in self.adj_matrix[node]:
            if ele not in self.visited:
                res_child = self.dfs(ele)
                res += res_child
        return res

    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        self.adj_matrix = defaultdict(list)
        self.visited = set()
        for indx , val in enumerate(bombs):
            x , y , r = val
            for sec_indx , sec_val in enumerate(bombs):
                sec_x , sec_y , sec_r  = sec_val
                if sec_indx != indx:
                    dis = math.sqrt((x - sec_x)**2 + (y - sec_y)**2)
                    if dis <= r :
                        self.adj_matrix[indx].append(sec_indx)
        
        bombs_c = 0
        for ele in range(len(bombs)):
            res = self.dfs(ele)
            bombs_c = max(res , bombs_c)
            self.visited = set()
        return bombs_c

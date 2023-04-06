from collections import defaultdict
class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        ele_dict = defaultdict(int)

        for first , second in edges:
            ele_dict[first] += 1
            ele_dict[second] += 1
            if ele_dict[i] == (len(edges)):
                return i

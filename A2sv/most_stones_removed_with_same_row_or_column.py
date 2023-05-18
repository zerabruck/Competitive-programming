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

    def union(self, ele1, ele2):
        rep_ele1 = self.find(ele1)
        rep_ele2 = self.find(ele2)
        if rep_ele1 != rep_ele2:
            if self.size[rep_ele1[1]] >= self.size[rep_ele2[1]]:
                self.size[rep_ele1[1]] += self.size[rep_ele2[1]]
                self.ele[rep_ele2] = rep_ele1
            elif self.size[rep_ele2[1]] >= self.size[rep_ele1[1]]:
                self.size[rep_ele2[1]] += self.size[rep_ele1[1]]
                self.ele[rep_ele1] = rep_ele2

    def removeStones(self, stones: List[List[int]]) -> int:
        self.ele = {((stones[i][0], stones[i][1]), i): ((stones[i][0], stones[i][1]), i) for i in range(len(stones))}
        self.size = [1] * len(stones)
        for cur_index in range(len(stones)):
            for ele_index in range(cur_index + 1, len(stones)):
                if stones[cur_index][0] == stones[ele_index][0] or stones[cur_index][1] == stones[ele_index][1]:
                    self.union(((stones[cur_index][0],stones[cur_index][1]), cur_index), ((stones[ele_index][0], stones[ele_index][1]), ele_index))
        groups = set()
        for i in self.ele.values():
            groups.add(self.find(i))
        return len(stones) - len(groups)

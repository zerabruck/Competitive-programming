from collections import defaultdict
class LockingTree:

    def __init__(self, parent: List[int]):
        self.parent = parent
        self.adj_matrix = defaultdict(list)
        for elem in range(1, len(parent)):
            self.adj_matrix[parent[elem]].append(elem)
        self.status = defaultdict(int)
        

    def lock(self, num: int, user: int) -> bool:
        if self.status[num] == 0:
            self.status[num] = user
            return True
        else:
            return False
        

    def unlock(self, num: int, user: int) -> bool:
        if self.status[num] == user:
            self.status[num] = 0
            return True
        else:
            return False
        

    def upgrade(self, num: int, user: int) -> bool:
        self.truth = False
        if self.status[num] == 0:
            if self.is_locked_ans(num):
                self.one_locked_desc(num)
                if self.truth:
                    self.status[num] = user
                    return True
        return False


    def is_locked_ans(self, num):
        current = num
        while current != -1:
            current = self.parent[current]
            if self.status[current] != 0:
                return False
        return True

    def one_locked_desc(self,num):
        self.status[num] = 0
        for ele in self.adj_matrix[num]:
            if self.status[ele] != 0:
                self.truth = True
            self.one_locked_desc(ele)     


# Your LockingTree object will be instantiated and called as such:
# obj = LockingTree(parent)
# param_1 = obj.lock(num,user)
# param_2 = obj.unlock(num,user)
# param_3 = obj.upgrade(num,user)

class Solution:
    def num_row(self, n):
        if n == self.numRows - 1:
            return
        n_ele = [1]
        # print(self.ele)
        if len(self.ele[n]) >= 2:
            for val in range(1, len(self.ele[n])):
                n_ele.append(self.ele[n][val] + self.ele[n][val - 1])
        n_ele.append(1)
        self.ele.append(n_ele)
        self.num_row(n + 1)
        
    def generate(self, numRows: int) -> List[List[int]]:
        self.numRows = numRows
        self.ele = [[1]]
        if numRows == 1:
            return [[1]]
        self.num_row(0)
        return self.ele

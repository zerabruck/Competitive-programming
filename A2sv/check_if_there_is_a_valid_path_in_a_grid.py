class Solution:
    def find(self,node):
        parent = self.rep[node]
        while parent != self.rep[parent]:
            parent = self.rep[parent]

        while node != self.rep[node]:
            temp = self.rep[node]
            self.rep[node] = parent
            node = temp
        return parent

    def union(self, row1, col1, row2, col2):
        node1_rep = self.find((row1, col1))
        node2_rep = self.find((row2, col2))
        if node1_rep != node2_rep:
            if self.size[node1_rep[0]][node1_rep[1]] >= self.size[node2_rep[0]][node2_rep[1]]:
                self.size[node1_rep[0]][node1_rep[1]] += self.size[node2_rep[0]][node2_rep[1]]
                self.rep[node2_rep] = node1_rep
            else:
                self.size[node2_rep[0]][node2_rep[1]] += self.size[node1_rep[0]][node1_rep[1]]
                self.rep[node1_rep] = node2_rep
    def end_point(self, row, col):
        value = self.grid[row][col]
        res = []
        if value == 1:
            res.append((row,col - 1))
            res.append((row, col + 1))
        elif value == 2:
            res.append((row - 1,col))
            res.append((row + 1, col))
        elif value == 3:
            res.append((row,col - 1))
            res.append((row + 1, col))
        elif value == 4:
            res.append((row + 1, col))
            res.append((row, col + 1))
        elif value == 5:
            res.append((row,col - 1))
            res.append((row - 1,col))
        else:
            res.append((row - 1,col))
            res.append((row, col + 1))
        return res
    def in_bound(self, row, col):
        return 0 <= row < len(self.grid) and 0 <= col < len(self.grid[0])

    def is_connected(self, row1, col1,row2, col2):
        if not self.in_bound(row1, col1) or not self.in_bound(row2, col2):
            return False
        endpoint1 = self.end_point(row1, col1)
        endpoint2 = self.end_point(row2, col2)
        if  (row1, col1) in endpoint2 and (row2, col2) in endpoint1:
            return True
        
        return False

    def hasValidPath(self, grid: List[List[int]]) -> bool:
        self.grid = grid
        self.rep = {}
        self.size = [[1 for i in range(len(grid[0]))] for i in range(len(grid))]
        for r_index, row in enumerate(grid):
            for c_index, col in enumerate(row):
                self.rep[(r_index, c_index)] = (r_index, c_index)
        for r_index, row in enumerate(grid):
            for c_index, col in enumerate(row):
                # up = (r_index - 1, c_index)
                if self.is_connected(r_index, c_index , r_index - 1, c_index):
                    self.union(r_index, c_index , r_index - 1, c_index)
                # down = (r_index + 1, c_index)
                if self.is_connected(r_index, c_index, r_index + 1, c_index):
                    # print("hioo")
                    self.union(r_index, c_index, r_index + 1, c_index)
                # left = (r_index, c_index + 1)
                if self.is_connected(r_index, c_index,r_index, c_index + 1):
                    self.union(r_index, c_index,r_index, c_index + 1)
                # right = (r_index, c_index - 1)
                if self.is_connected(r_index, c_index,r_index, c_index - 1):
                    self.union(r_index, c_index,r_index, c_index - 1)
        return self.find((0, 0)) ==  self.find((len(grid) - 1, len(grid[0]) - 1))

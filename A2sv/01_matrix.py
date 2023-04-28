class Solution:
    def is_bound(self, row, col, mat):
        return 0 <= row < len(mat) and 0 <= col < len(mat[0])
        
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        # (row, col, layer)
        quee = deque()
        visited = set()
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for row in range(len(mat)):
            for col in range(len(mat[0])):
                if mat[row][col] == 0:
                    quee.append((row, col,0))
                    visited.add((row,col))
        while quee:
            val = quee.popleft()

            for row, col in directions:
                row_d = row + val[0]
                col_d = col + val[1]

                if self.is_bound(row_d, col_d , mat) and (row_d, col_d) not in visited:
                    mat[row_d][col_d] = val[2] + 1
                    quee.append((row_d, col_d, val[2] + 1))
                    visited.add((row_d,col_d))
        return mat 

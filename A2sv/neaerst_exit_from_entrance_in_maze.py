class Solution:
    def is_border(self, row_d , col_d , maze):
        return row_d == 0 or row_d == (len(maze) - 1) or col_d == 0 or col_d == (len(maze[0]) - 1)

    def in_bound(self, row, col, maze):
        return 0 <= row < len(maze) and 0 <= col < len(maze[0])

    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        # (row, col, layer)
        que = deque([(entrance[0], entrance[1], 0)]) 
        maze[entrance[0]][entrance[1]] = "+"

        while que:
            node = que.popleft()
            for row, col in directions:
                row_d = row + node[0]
                col_d = col + node[1]
                if self.in_bound(row_d, col_d, maze) and maze[row_d][col_d] == ".":        
                    que.append((row_d, col_d, node[2] + 1))
                    maze[row_d][col_d] = "+"
                    if self.is_border(row_d, col_d, maze):
                        return node[2] + 1
        return -1

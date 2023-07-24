class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        tr_path = triangle[-1]
        for row in range(len(triangle) - 2, -1, -1):
            new_path = [inf] * len(triangle[row])
            for col in range(len(tr_path)):
                if col < len(new_path):
                    value = tr_path[col] + triangle[row][col]
                    new_path[col] = min(value, new_path[col])
                if col - 1 >= 0:
                    value = tr_path[col] + triangle[row][col - 1]
                    new_path[col - 1] = min(value, new_path[col - 1])
            tr_path = new_path
        return tr_path[0] 

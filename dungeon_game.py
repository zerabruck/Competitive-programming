class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        row,col = len(dungeon), len(dungeon[0])
        @lru_cache(None)
        def dp(x,y):
            if x == row-1 and y==col-1:
                return max(1, -dungeon[x][y] + 1)
            ans = inf

            if x+1 < row:
                ans = min(ans, dp(x+1, y))
            if y+1 < col:
                ans = min(ans, dp(x, y+1))
            
            ans += -dungeon[x][y]

            return max(1, ans)
        return dp(0,0)

class Solution:
    def min_cost(self, stair):
        if stair < 2:
            return self.cost[stair]
        
        if stair not in self.dicto:
            first_cost = self.min_cost(stair - 1)
            second_cost = self.min_cost(stair - 2)
            low_cost = min(first_cost, second_cost)
            self.dicto[stair] = low_cost + self.cost[stair]
        return self.dicto[stair]
 
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        self.dicto = {}
        self.cost = cost
        first = self.min_cost(len(cost) - 1)
        second = self.min_cost(len(cost) - 2)
        return min(first, second)

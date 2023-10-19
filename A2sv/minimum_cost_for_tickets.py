class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp = [0] * len(days)
        dp[0] = min(costs)
        for day in range(1, len(days)):
            min_cost = inf
            one_day = True
            seven_day = True
            thrity_day = True
            for prev in range(day, -1, -1):
                if one_day and days[prev] <= days[day] - 1:
                    min_cost = min(min_cost, dp[prev] + costs[0])
                    one_day = False    
                if seven_day and days[prev] <= days[day] - 7:
                    min_cost = min(min_cost, dp[prev] + costs[1])
                    seven_day = False
                if thrity_day and days[prev] <= days[day] - 30:
                    min_cost = min(min_cost, dp[prev] + costs[2])
                    thrity_day = False

            if one_day:
                min_cost = min(min_cost, costs[0])
            if seven_day:
                min_cost = min(min_cost, costs[1])
            if thrity_day:
                min_cost = min(min_cost, costs[2])
            dp[day] = min_cost

        return dp[-1]      

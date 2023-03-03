class Solution:
    def day_checker(self , capacity , weights):
        inner_days = 0
        cur_capacity = 0

        for weight in weights: 
            cur_capacity += weight

            if cur_capacity > capacity:
                inner_days += 1
                cur_capacity = weight

        inner_days += 1

        return inner_days

        

    def shipWithinDays(self, weights: List[int], days: int) -> int:

        high = sum(weights)
        low = max(weights)
        max_capacity = inf

        while low <= high :
            mid = (high + low) // 2 
            
            if self.day_checker(mid , weights) > days:
                low = mid + 1
                

            elif self.day_checker(mid , weights) < days :
                high = mid - 1

                max_capacity = min(max_capacity , mid)
                

            else:
                max_capacity = min(max_capacity , mid)
                high = mid - 1

        return max_capacity

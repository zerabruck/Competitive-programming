class Solution:
    def prime_serach(self, left , right):
        nums = [True] * (right + 1)
        d = 2
        while d * d <= right:
            if nums[d]:
                val = d
                while val * d <= right:
                    nums[val * d] = False
                    val += 1
            d += 1
        nums[1] = False
        res = []
        for indx in range(left , right + 1):
            if nums[indx]:
                res.append(indx)
        return res
        
    def closestPrimes(self, left: int, right: int) -> List[int]:
        primes = self.prime_serach(left , right)
        if len(primes) < 2:
            return [-1 , -1]

        res = []
        min_val = right
        for indx in range(1,len(primes)):
            diff = primes[indx] - primes[indx - 1]
            if min_val > diff:
                res = [primes[indx - 1] , primes[indx]]
                min_val = diff
        return res

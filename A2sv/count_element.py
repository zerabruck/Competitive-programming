from itertools import combinations 
from collections import Counter 
class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:

        dicto = Counter(deliciousness)
        result = 0
        for first_meal in deliciousness:
            dicto[first_meal] -= 1
            
            for j in range(22):
                second_meal = 2**j - first_meal
                if second_meal in dicto:
 
                    result += dicto[second_meal]

                    
        return result % (10 ** 9 + 7 )

                    

class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        sec_int = num // 3
        consectives= [sec_int -1, sec_int , sec_int + 1]
        
        if sum(consectives) == num:
            return consectives
        return []


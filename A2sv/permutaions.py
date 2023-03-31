class Solution:
    def go_through(self , nums , bit_set , traveld):

        if len(traveld) == len(nums) :
            self.ele.append(list(traveld.copy()))
            return 
        
        for indx in range( len(nums)):
            val = bit_set >> indx 
            if val & 1 == 0:
                traveld.append(nums[indx])
                bit_set |= 1 << indx 
                self.go_through(nums, bit_set , traveld)
                bit_set ^= 1 << indx
                traveld.pop()
    
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.ele = []
        self.go_through(nums , 0 , [])
        return self.ele

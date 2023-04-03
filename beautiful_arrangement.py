class Solution:
    def go_through(self , nums , bit_set , traveld):

        if len(traveld) == len(nums) :           
            self.count += 1
            return 
        
        for indx in range( len(nums)):
            val = bit_set >> indx 
            if val & 1 == 0:
                bit_set |= 1 << indx 
                if nums[indx] % (len(traveld) + 1) == 0 or (len(traveld) + 1) % nums[indx] == 0:

                    traveld.append(nums[indx])
                    
                    self.go_through(nums, bit_set , traveld)
                    traveld.pop()
                bit_set ^= 1 << indx
    def countArrangement(self, n: int) -> int:
        self.count = 0
        nums = [i for i in range(1 , n + 1)]
        self.go_through(nums , 0 , [])

        return self.count

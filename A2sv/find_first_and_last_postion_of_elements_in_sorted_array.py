class Solution:
    def high_search(self , nums , target , position ) :
        high = len(nums) - 1
        low = 0
        while low <= high :
            mid = (high + low) // 2
            if nums[mid] == target :
                position[1] = mid
                low = mid + 1

            elif nums[mid] > target :
                high = mid - 1
            elif nums[mid] < target :
                low = mid + 1
    def low_search(self , nums , target , position ) :
        high = len(nums) - 1
        low = 0
        while low <= high :
            mid = (high + low) // 2
            if nums[mid] == target :
                position[0] = mid
                high = mid - 1

            elif nums[mid] > target :
                high = mid - 1
            elif nums[mid] < target :
                low = mid + 1

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        postion = [-1 , -1 ]
        self.high_search(nums , target , postion)
        self.low_search(nums , target , postion)
        return postion

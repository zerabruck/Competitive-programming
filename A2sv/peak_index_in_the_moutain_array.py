class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        high = len(arr) - 1 
        low = 0
        while low <= high :
            mid = (low + high) // 2
            if arr[mid + 1 ] > arr[mid] :
                low = mid + 1 

            elif arr[ mid - 1 ] < arr[mid] > arr[ mid + 1] :
                return mid

            elif arr[mid - 1 ] > arr[mid] :
                high = mid - 1

class Solution:
    def merger(self , nums1 , nums2):
        new_arr = []
        first = 0
        second = 0
        while first < len(nums1) and second < len(nums2):
            if nums1[first] <= nums2[second]:
                new_arr.append(nums1[first])
                first += 1
            else:
                new_arr.append(nums2[second])
                second += 1

        new_arr.extend(nums1[first:])
        new_arr.extend(nums2[second:])
        return new_arr

    def counter (self , nums1 , nums2 , diff):
        count = 0
        first = 0
        second = 0
        while first < len(nums1) and second < len(nums2):
            if nums1[first] <= nums2[second] + diff:
                first += 1
                count += 1
            else:
                second += 1
                count += first

        reminder = len(nums2) - (second + 1)
        reminder *= first
        count += reminder
        return count

    def merge_sort(self , first , last , nums , counter , diff):
        if first == last:
            return [nums[first]]
        mid = (first + last) // 2
        left = self.merge_sort(first , mid , nums , counter , diff)
        right = self.merge_sort(mid + 1 , last , nums , counter , diff)
        
        count = self.counter(left , right , diff )
        counter[0] += count
        return self.merger(left , right)
               

    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        
        # steps i need to follow 
        # first merge the two arrays
        # do merge sort 
        # in each level implemnt merger and counter that satisfies right + diff > left
        for index in range(0 , len(nums1)):
            nums1[index] -= nums2[index]

        counter = [0]
        self.merge_sort(0 , len(nums1) - 1 , nums1, counter , diff)
        return counter[0]

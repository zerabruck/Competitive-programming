class Solution:
    def right_smaller(self , left_arr , right_arr , counter):
        left = 0
        right = 0
        while left < len(left_arr) and right < len(right_arr):
            if left_arr[left] > right_arr[right]:
                right += 1
            else:
                indx = left_arr[left][1]
                counter[indx] += right
                left += 1

        for indx_ele in range(left , len(left_arr)):
            indx = left_arr[indx_ele][1]
            counter[indx] += right

    def merger(self , nums1 , nums2):
        new_arr = []
        first = 0
        second = 0
        while first < len(nums1) and second < len(nums2):
            if nums1[first][0] <= nums2[second][0]:
                new_arr.append(nums1[first])
                first += 1
            else:
                new_arr.append(nums2[second])
                second += 1

        new_arr.extend(nums1[first:])
        new_arr.extend(nums2[second:])
        return new_arr

    def merge_sort(self , first , last , nums , counter):
        if first == last:
            return [nums[first]]
        mid = (first + last) // 2
        left_arr = self.merge_sort(first , mid , nums , counter)
        right_arr = self.merge_sort(mid + 1 , last , nums , counter )
        
        self.right_smaller(left_arr , right_arr , counter)
        return self.merger(left_arr , right_arr)

    def countSmaller(self, nums: List[int]) -> List[int]:
        for indx in range(len(nums)):
            nums[indx] = (nums[indx] , indx)
        counter = [0] * len(nums)
        self.merge_sort(0 , len(nums) - 1 , nums , counter)
        return counter

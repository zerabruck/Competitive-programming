class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        maxi = arr[-1]
        arr[-1] = -1
        for index in range(len(arr) -2 ,-1,-1):
            value = arr[index]
            arr[index] = maxi
            if value > maxi :
                maxi = value
        return arr



    
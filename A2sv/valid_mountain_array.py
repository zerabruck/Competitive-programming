class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        prev = arr[0]
        flag = False
        count = 0
        if len(arr) < 3:
            return False
        for indx,i in enumerate(arr[1:]):
            if flag:
                if prev <= i:
                    return False
                if indx == len(arr) -2  and count != 0 :
                    return True
                else:
                    prev = i
            elif i < prev:
                prev = i
                flag = True
                if indx == len(arr) -2 and count != 0 :
                    return True 

            elif i == prev:
                return False

            else:
                count += 1
                prev = i

        return False


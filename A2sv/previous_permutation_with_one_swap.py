class Solution:
    def prevPermOpt1(self, arr: List[int]) -> List[int]:      
        for index in range(len(arr) - 2, -1, -1):
            mini = index
            for inner in range(index, len(arr)):                
                if arr[index] > arr[inner]:
                    if mini == index:
                        mini = inner
                    elif arr[mini] < arr[inner]:
                        mini = inner
            if mini != index:
                arr[index], arr[mini] = arr[mini], arr[index]
                return arr
        return arr

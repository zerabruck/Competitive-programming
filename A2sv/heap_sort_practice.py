#User function Template for python3

class Solution:
    def heapify(self,arr, n, i):
        current = i
        while current < n:
            left_child = (2 * current) + 1
            right_child = (2 * current) + 2
            smallest = current
            if left_child < n and arr[left_child] >= arr[smallest]:
                smallest = left_child
            if right_child < n and arr[right_child] > arr[smallest]:
                smallest = right_child
            if smallest == current:
                break
            arr[smallest], arr[current] = arr[current], arr[smallest]
            current = smallest
    
    #Function to build a Heap from array.
    def buildHeap(self,arr,n):
        # code here
        for index in range(len(arr)//2 - 1 , -1, -1):
            self.heapify(arr, n , index)
        
    
    #Function to sort an array using Heap Sort.
    def HeapSort(self, arr, n):
        self.buildHeap(arr, n)
        for index in range(n - 1 , 0, -1):
            arr[0], arr[index] = arr[index], arr[0]
            self.heapify(arr, index , 0)
        #code here

#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Mohit Kumara

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        Solution().HeapSort(arr,n)
        print(*arr)

# } Driver Code Ends

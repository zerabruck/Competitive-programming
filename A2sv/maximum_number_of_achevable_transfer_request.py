class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        ans = 0
        degree = [0 for _ in range(n)]

        def maxRequest(index, count):
            if(index == len(requests)):
                for i in range(n):
                    if(degree[i]):
                        return
                nonlocal ans
                ans = max(ans, count)
                return

            degree[requests[index][0]] -= 1
            degree[requests[index][1]] += 1

            maxRequest(index + 1, count + 1)

            degree[requests[index][0]] += 1
            degree[requests[index][1]] -= 1

            maxRequest(index + 1, count)

        maxRequest(0, 0)

        return ans

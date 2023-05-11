from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = defaultdict(list)
        in_degree = [0 for i in range(numCourses)]

        for course, preCourse in prerequisites:
            adj_list[preCourse].append(course)
            in_degree[course] += 1

        quee = deque()
        count = 0
        for i in range(len(in_degree)):
            if in_degree[i] == 0:
                quee.append(i)

        while quee:
            val = quee.popleft()
            count += 1

            for nebor in adj_list[val]:
                in_degree[nebor] -= 1
                if in_degree[nebor] == 0:
                    quee.append(nebor)

        return count == numCourses

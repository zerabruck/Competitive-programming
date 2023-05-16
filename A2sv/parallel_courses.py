from collections import defaultdict,deque
def parallelCourses(n, prerequisites):
    # print(prerequisites)
    adj_list = defaultdict(list)
    in_degree = [0] * n
    courses = deque()
    n_courses = set()
    semsiters = 0 
     
    for preC, course in prerequisites:
        adj_list[preC - 1].append(course - 1)
        in_degree[course - 1] += 1

    for index in range(len(in_degree)):
        if in_degree[index] == 0:
            courses.append((index, 1))

    while courses:
        crs = courses.popleft()
        n_courses.add(crs[0])
        semsiters = max(semsiters, crs[1])
        for nebor in adj_list[crs[0]]:
            in_degree[nebor] -= 1
            if in_degree[nebor] == 0:
                courses.append((nebor, crs[1] + 1))
    if len(n_courses) != n:
        return -1
    return semsiters

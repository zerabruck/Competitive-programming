class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        visited = set(["0000"])
        que = deque([(0,"0000")])
        if target == '0000':
            return 0
        if '0000' in deadends:
            return -1
        
        while que:
            val = que.popleft()
            for i in range(4):
                locks = int(val[1][i])
                lock_add = (locks + 1) % 10
                add_str = val[1][:i] + str(lock_add) + val[1][i + 1: ]
                if add_str not in visited and add_str not in deadends:
                    que.append((val[0] + 1, add_str))
                    visited.add(add_str)
                    if add_str == target:
                        return val[0] + 1
            for i in range(4):
                locks = int(val[1][i])
                lock_sub = (locks - 1) % 10
                sub_str = val[1][:i] + str(lock_sub) + val[1][i + 1: ]
                if sub_str not in visited and sub_str not in deadends:
                    que.append((val[0] + 1, sub_str))
                    visited.add(sub_str)
                    if sub_str == target:
                        return val[0] + 1
        return -1

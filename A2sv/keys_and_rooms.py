class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        quee = deque([0])
        visited = set([0])
        while quee:
            val = quee.popleft()
            for ele in rooms[val]:
                if ele not in visited:
                    visited.add(ele)
                    quee.append(ele)
                    if len(visited) == len(rooms): return True
        return len(visited) == len(rooms)

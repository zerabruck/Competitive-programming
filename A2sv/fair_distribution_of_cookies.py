class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        self.cok = cookies
        self.min_cok = inf
        self.unfair_finder([0 for i in range(k)] , 0)
        return self.min_cok

    def unfair_finder(self , visited , idx) :
        if idx >= len(self.cok) :
            val = max(visited)
            self.min_cok = min(val , self.min_cok)
            return

        else:
            for i in range(len(visited)):
                visited[i] += self.cok[idx]
                if visited[i] < self.min_cok:
                    self.unfair_finder(visited , idx + 1)
                visited[i] -= self.cok[idx]

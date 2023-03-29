class Solution:
    def check(self , traverse):
        for ele in traverse:
            int_ele = int(ele)
            str_ele = str(int_ele)
            if int_ele > 255 or len(str_ele) != len(ele):
                return False
        return True 

    def ip_poss(self , traverse , string ):
        if len(traverse) == 4:
            if len(string) == 0 and self.check(traverse):
                ips = '.'.join(traverse)
                self.valid_ip.append(ips)
            return 
                
        for i in range(len(string)):
            traverse.append(string[:i + 1])
            self.ip_poss(traverse , string[i + 1 :])
            traverse.pop()

    def restoreIpAddresses(self, s: str) -> List[str]:
        self.valid_ip = []
        self.ip_poss([] , s)
        return self.valid_ip

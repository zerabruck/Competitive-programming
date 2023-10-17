class Solution:
    def is_ipv4(self,ip):
        ips = ip.split('.')
        if len(ips) != 4:
            return False
        for ele in ips:
            try:
                if int(ele) > 255 or int(ele) < 0:
                    return False
                first = len(ele)
                second = int(ele)
                if first > len(str(second)):
                    return False
            except:
                return False
        return True
    def is_ipv6(self, ip):
        ips = ip.split(':')
        if len(ips) != 8:
            return False
        char_set = set()
        for i in range(ord('a'), ord('f') + 1):
            char_set.add(i)
        for i in range(ord('A'), ord('F') + 1):
            char_set.add(i)
        for i in range(ord('0'), ord('9') + 1):
            char_set.add(i)

        for single in ips:
            if not single:
                return False
            if len(single) > 4:
                return False
            for char in single:
                if ord(char) not in char_set:
                    return False
        return True

    def validIPAddress(self, queryIP: str) -> str:
        if self.is_ipv4(queryIP):
            return "IPv4"
        elif self.is_ipv6(queryIP):
            return "IPv6"
        else:
            return "Neither"        

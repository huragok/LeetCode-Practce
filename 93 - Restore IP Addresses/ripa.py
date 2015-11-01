class Solution:
    # @param {string} s
    # @return {string[]}
    def restoreIpAddresses(self, s):
        return self._restoreIpAddresses(s, 4)
    
    def _restoreIpAddresses(self, s, n_seg):
        if s == "":
            return []
        elif n_seg == 1:
            if s == "0" or (s[0] != "0" and 0 <= int(s) <= 255):
                return [s]
            else:
                return []
        else:
            n = len(s)
            addresses = []
            for n_digits in range(1, min(3, n) + 1):
                head = s[0:n_digits]
                if head == "0" or (s[0]!= "0" and 0 <= int(head) <= 255):
                    sub_addresses = self._restoreIpAddresses(s[n_digits:], n_seg - 1)
                    for sa in sub_addresses:
                        addresses.append(s[0:n_digits]+"."+sa)
                        
            return addresses
            
if __name__ == "__main__":
    s = "010010"
    print(Solution().restoreIpAddresses(s))

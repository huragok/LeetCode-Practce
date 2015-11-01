class Solution:
    # @param {string} s
    # @return {integer}
    def numDecodings(self, s):
        n = len(s)
        
        if n < 1 or int(s[0]) == 0:
            return 0
        elif n < 2:
            return 1
                
        ways_prev = 1
        ways = 1
        ptr = 1
        
        while ptr < n:
            ways_new = 0
            if int(s[ptr]) > 0:
                ways_new += ways
            if  0 < int(s[ptr - 1: ptr + 1]) < 27 and s[ptr - 1] != "0":
                ways_new += ways_prev
            ways_prev = ways
            ways = ways_new
            ptr += 1
        
        return ways
        
        
if __name__ == "__main__":
    s = "101"
    print(Solution().numDecodings(s))
        

             

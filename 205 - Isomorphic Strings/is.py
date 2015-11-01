class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        m = len(s)
        if m != len(t):
            return False
            
        map_st = {}
        map_ts = {}
        for idx, c in enumerate(s):
            if c in map_st:
                if map_st[c] != t[idx]:
                    return False
            elif t[idx] in map_ts:
                return False
            else:
                map_st[c] = t[idx]
                map_ts[t[idx]] = c
                
        return True
        
if __name__ == "__main__":
    s = 'dgg'
    t = 'abb'
    print(Solution().isIsomorphic(s, t))

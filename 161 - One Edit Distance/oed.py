import itertools

class Solution:
    # @param {string} s
    # @param {string} t
    # @return {boolean}
    def isOneEditDistance(self, s, t):
        m = len(s)
        n = len(t)
        if m - n > 1 or m - n < -1:
            return False
            
        if m == n: # There can only be a replacement
            count_diff = 0
            for c_s, c_t in itertools.izip(s, t):
                if c_s != c_t
                    count_diff += 1
                    if count_diff > 1:
                        return False
        else:
            if m < n: # Make sure m is the longer one
                s, t = t, s
                m, n = n, m
                
            idx_l = 0
            while idx_l < n:
                if s[idx_l] != t[idx_l]:
                    break
                idx_l += 1
            if idx_l == n:
                return True
                
            idx_r = n - 1
            while idx_r >= 0:
                if s[idx_r] != t[idx_r]:
                    break
                idx_r -= 1
                
            if idx_r == -1:
                return True
                
            return idx_l - idx_r == 1
            
       

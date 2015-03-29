#!/usr/bin/env python

class Solution:
    # @return a string
    def longestCommonPrefix(self, strs):
        if not strs:
            return ''
        min_len = min((len(s) for s in strs)) # The minimum length
        n_strs = len(strs)
        
        idx = 0
        len_prefix = 0
        flag = True 
        while idx < min_len and flag:
            c = strs[0][idx]
            for i_strs in range(1, n_strs):
                if c != strs[i_strs][idx]:
                    flag = False
                    break;
            if flag:
                idx += 1
                len_prefix += 1
                
        return strs[0][0:len_prefix]
        
if __name__=="__main__":
    sol = Solution()
    strs = ('fuck you', 'fuck me', 'fuuu')
    print(sol.longestCommonPrefix(strs))        

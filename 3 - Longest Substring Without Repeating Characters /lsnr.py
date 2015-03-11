#!/usr/bin/env python3
import string

class Solution:
    # @return an integer
    def lengthOfLongestSubstring(self, s):
        pos = {s: None for s in string.printable}
        length = 1
        head = 0
        tail = head + 1
        len_s = len(s)
        if len_s == 0:
            return 0
        pos[s[0]] = 0
        while tail < len_s:
            if pos[s[tail]] is None: # No repetition
                pos[s[tail]] = tail
            else: # Repetition
                length_current = tail - head
                if length_current > length:
                    length = length_current
                
                for i in range(head, pos[s[tail]]):
                    pos[s[i]] = None
                head = pos[s[tail]] + 1
                pos[s[tail]] = tail
                
                
            tail += 1
            #print((head, tail))
        length_current = tail - head
        if length_current > length:
            length = length_current
            
        return length
        
if __name__ == "__main__":
    s = "aab"
    print("LSNR = {0}".format(Solution().lengthOfLongestSubstring(s)))

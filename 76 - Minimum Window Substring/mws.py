import collections

class Solution:
    # @param {string} s
    # @param {string} t
    # @return {string}
    def minWindow(self, s, t):
        
        n = len(s)
        l = 0 # Current window is [l:r]
        r = 0
        
        min_window = n + 1
        answer = ""
        
        # The number of each character that is not covered by the current window
        char_left = collections.defaultdict(int)
        for c in t:
            char_left[c] += 1
        uncovered = len(t) # The number of characters in t that is not covered by the current window 
            
        while r <= n:
            if uncovered == 0: # If all the characters are already in the window
                if r - l < min_window:
                    min_window = r - l
                    answer = s[l:r]
                
                c_pop = s[l]
                if c_pop in char_left:
                    char_left[c_pop] += 1
                    if char_left[c_pop] > 0:
                        uncovered += 1
                l += 1
            else:
                if r == n:
                    break      
                c_push = s[r]
                if c_push in char_left:
                    char_left[c_push] -= 1
                    if char_left[c_push] >= 0:
                        uncovered -= 1
                r += 1
            print("______________________________")
            print("min_window = {0}".format(min_window))
            print("l, r = {0}, {1}".format(l, r))
            print(char_left)
            print("uncovered = {0}".format(uncovered))
            print("answer = {0}".format(answer))
                
        return answer
        
if __name__ == "__main__":
    s = "ADOBECODEBANC"
    t = "ABC"
    s = "cabwefgewcwaefgcf"
    t = "cae"
    print(Solution().minWindow(s, t))
        
            
        

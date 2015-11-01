class Solution:
    # @param {string} s
    # @return {integer}
    def lengthOfLastWord(self, s):
        n = len(s)
        if n == 0:
            return 0
        
        # locate the end of the last word
        for i in range(n - 1, -1, -1):
            if s[i] != ' ':
                break
        if i == 0 and s[0] = ' ':
            return 0
            
        # locate the start of the last word
        for j in range(i, -1, -1):
            if s[j] == ' ':
                break
        
        if j == 0 and s[0] != ' ':
            j = -1
        
        return i - j                

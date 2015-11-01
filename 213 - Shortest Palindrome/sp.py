class Solution(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        n0 = len(s)
        if n0 <= 1:
            return s
        
        s_mirrored = s + '_' + s[-1::-1]
        n = 2 * n0 + 1
        pi = [0] * n
        k = -1
        for q in range(1, n):
            while k >= 0 and s_mirrored[k + 1] != s_mirrored[q]:
                k = pi[k] - 1
                
            if s_mirrored[k + 1] == s_mirrored[q]:
                k = k + 1
                
            pi[q] = k + 1
        #print(pi)    
        return s[-1 : k : -1] + s
        
if __name__ == "__main__":
    s = "abcd"
    print(Solution().shortestPalindrome(s))
        
        

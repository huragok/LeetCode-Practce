class Solution:
    # @param {string} s
    # @return {integer}
    def minCut(self, s):
        n = len(s)
        cut = [-1] + range(n) # cut[i] is the min cut for s[0:i]
        

        # Start the iteration
        for i in range(1, n + 1):
        
            d = 0 #  odd length of palindrome centered at s[i-1]
            while i - 1 - d >= 0 and i + d <= n:
                if s[i-1+d] != s[i-1-d]:
                    break
                cut[i + d] = min([cut[i + d], cut[i-1-d] + 1])
                d += 1
            
            
            if i < n and s[i-1] == s[i]:#  even length of palindrome whose left center is at s[i-1] 
                d = 1 
                while i - d >= 0 and i + d <= n:
                    if s[i-1+d] != s[i-d]:
                        break
                    cut[i + d] = min([cut[i + d], cut[i-d] + 1])
                    d += 1 
        return cut[n]
        
if __name__ == "__main__":
    s = "aab"
    print(Solution().minCut(s))

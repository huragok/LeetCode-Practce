class Solution:
    # @param {string} s1
    # @param {string} s2
    # @param {string} s3
    # @return {boolean}
    def isInterleave(self, s1, s2, s3):
        m = len(s1)
        n = len(s2)
        l = len(s3)
        if l != m + n:
            return False
        
        if m == 0:
            return s2 == s3
        elif n == 0:
            return s1 == s3
        
        d = [False] * (n + 1) # d[i][j] indicates whether s1[0:i] and s2[0:j] interleave into s3[0:i+j]
        
        # Initialization
        d[0] = True
        j = 0
        while j < n and s2[j] == s3[j]:
            d[j + 1] = True
            j += 1
        #print(d)    
        # Start the iteration
        for i in range(1, m + 1):
            d[0] = True if (d[0] and s1[i - 1] == s3[i - 1]) else False
            for j in range(1, n + 1):
                d[j] = (d[j] and s1[i - 1] == s3[i + j - 1]) or (d[j - 1] and s2[j - 1] == s3[i + j - 1])
            #print(d)
                
        return d[n]
        
if __name__ == "__main__":
    s1 = "aabcc"
    s2 = "dbbca"
    s3 = "aadbbbaccc"
    print(Solution().isInterleave(s1, s2, s3))
            

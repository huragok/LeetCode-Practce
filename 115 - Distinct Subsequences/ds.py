class Solution:
    # @param {string} s
    # @param {string} t
    # @return {integer}
    def numDistinct(self, s, t):
        m = len(s)
        n = len(t)
        
        c = [0] * (m + 1) # c[m, n] is the count of distinct of T[0:n] in S[0:m] where T[n-1] must appear at S[m-1]
        
        # Initialization for n == 1
        for row in range(1, m + 1):
            if s[row - 1] == t[0]:
                c[row] = 1
                
        # Start the iteration
        for col in range(2, n + 1):
            c_cumsum = 0
            for row in range(1, m + 1):
                temp = c[row]
                if s[row - 1] == t[col - 1]:
                    c[row] = c_cumsum
                else:
                    c[row] = 0
                c_cumsum += temp
                
        return sum(c)
        
if __name__ == "__main__":
    s = "rabbbit"
    t = "rabbit"
    print(Solution().numDistinct(s, t))
    

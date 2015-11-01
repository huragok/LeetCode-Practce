class Solution:
    # @param {integer} n
    # @return {integer}
    def numTrees(self, n):
        count = [[0] * (n + 1) for row in range(n + 1)]
        
        # Initialization
        for l in range(n + 1):
            count[l][l] = 1
            
        for l in range(n):
            count[l][l + 1] = 1
            
        # Iteration
        for d in range(2, n + 1):
            for l in range(n - d + 1):
                r = l + d
                for i in range(l, r):
                    count[l][r] += count[l][i] * count[i+1][r]
                    
        return count[0][n]
        
if __name__ == "__main__":
    n = 3
    print(Solution().numTrees(n))

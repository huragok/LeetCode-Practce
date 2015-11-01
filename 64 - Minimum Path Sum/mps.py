class Solution:
    # @param {integer[][]} grid
    # @return {integer}
    def minPathSum(self, grid):
        m = len(grid)
        if m == 0:
            return 0
        n = len(grid[0])
        if n == 0:
            return 0
            
        min_sum = [0] * n
        
        # Initialization
        cumsum = 0
        for col in range(n - 1, -1, -1):
            cumsum += grid[m - 1][col]
            min_sum[col] = cumsum
            
        # Start the iteration
        for row in range(m - 2, -1, -1):
            min_sum[n - 1] += grid[row][n - 1]
            for col in range(n - 2, -1, -1):
                min_sum[col] = min((min_sum[col], min_sum[col + 1])) + grid[row][col]
                
        return min_sum[0]
            

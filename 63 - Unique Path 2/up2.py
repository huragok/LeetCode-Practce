class Solution:
    # @param {integer[][]} obstacleGrid
    # @return {integer}
    def uniquePathsWithObstacles(self, obstacleGrid):
        m = len(obstacleGrid)
        if m == 0:
            return 0
        n = len(obstacleGrid[0])
        if n == 0:
            return 0
        
        countUniquePath = [[0] * n for row in range(m)]
        # Initialization
        if obstacleGrid[m - 1][n - 1] == 1:
            return 0
            
        for row in range(m - 1, -1, -1):
            if obstacleGrid[row][n - 1] == 1:
                countUniquePath[row][n - 1] = 0
                break
            else:
                countUniquePath[row][n - 1] = 1
        for row_rest in range(row - 1, -1, -1):
            countUniquePath[row_rest][n - 1] = 0
            
        for col in range(n - 1, -1, -1):
            if obstacleGrid[m - 1][col] == 1:
                countUniquePath[m - 1][col] = 0
                break
            else:
                countUniquePath[m - 1][col] = 1
        for col_rest in range(col - 1, -1, -1):
            countUniquePath[m - 1][col_rest] = 0
            
        # Compute recursively
        for row in range(m - 2, -1, -1):
            for col in range(n - 2, -1, -1):
                if obstacleGrid[row][col] == 1:
                    countUniquePath[row][col] = 0
                else:
                    countUniquePath[row][col] = countUniquePath[row][col + 1] + countUniquePath[row + 1][col]
                    
        
        return countUniquePath[0][0]

if __name__ == "__main__":
    obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
    print(Solution().uniquePathsWithObstacles(obstacleGrid))

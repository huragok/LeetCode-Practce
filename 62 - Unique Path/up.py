class Solution:
    # @param {integer} m
    # @param {integer} n
    # @return {integer}
    def uniquePaths(self, m, n):
        if m == 0 or n == 0:
            return 0
        elif m == 1 or n == 1:
            return 1

        count_up = [[0] * n for row in range(m)] # count_up[i][j] is the number of unique path to the destination from grid ij
        # Initialization
        for row in range(m):
            count_up[row][n - 1] = 1
        for col in range(n):
            count_up[m - 1][col] = 1

        # Start the iteration

        for row in range(m - 2, -1, -1):
            for col in range(n - 2, -1, -1):
                count_up[row][col] = count_up[row][col + 1] + count_up[row + 1][col]

        return count_up[0][0]

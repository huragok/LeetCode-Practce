class Solution:
    # @param triangle, a list of lists of integers
    # @return an integer
    def minimumTotal(self, triangle):
        n = len(triangle) # Size of the triangle
        if n == 0:
            return None
            
        min_sum = triangle[n - 1][:]
        for row in range(n - 2, -1, -1):
            for col in range(row + 1):
                min_sum[col] = triangle[row][col] + min([min_sum[col], min_sum[col + 1]])
                
        return min_sum[0]
        
if __name__ == "__main__":
    triangle = [[2], [3,4], [6,5,7], [4,1,8,3]]
    print(Solution().minimumTotal(triangle))

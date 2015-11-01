class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        m = len(matrix)
        if m == 0:
            return 0
        n = len(matrix[0])
        if n == 0:
            return 0
            
        a = [0] * n # wa(i, j) is the edge length of the maximum square whose bottom right corner is on matrix[i, j]
        max_square = 0
        # Initialization
        a[0] = 1 if matrix[0][0] == '1' else 0
        max_square = max([max_square, a[0] ** 2])
        for col in range(1, n):
            a[col] = 1 if matrix[0][col] == '1' else 0
            max_square = max([max_square, a[col] ** 2])
        print(a)
        # Start the iteration
        for row in range(1, m):
            a_prev = a[:]
            a[0] = 1 if matrix[row][0] == '1' else 0
            max_square = max([max_square, a[0] ** 2])
            for col in range(1, n):
                a[col] = min(min([a[col - 1], a_prev[col - 1]]), a[col]) + 1 if matrix[row][col] == '1' else 0
                max_square = max([max_square, a[col] ** 2])
            print(a)
        return max_square
        
if __name__ == "__main__":
    #matrix  = [['1']]
    #matrix = [['1', '0', '1', '0', '0'],
              #['1', '0', '1', '1', '1'],
              #['1', '1', '1', '1', '1'],
              #['1', '0', '0', '1', '0']]
    matrix = ["1010",
              "1011",
              "1011",
              "1111"]
    print(Solution().maximalSquare(matrix))
        

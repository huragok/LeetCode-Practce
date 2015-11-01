class Solution:
    # @param {integer[][]} matrix
    # @return {void} Do not return anything, modify matrix in-place instead.
    def setZeroes(self, matrix):
        m = len(matrix)
        if m == 0:
            return
        n = len(matrix[0])
        
        fr = False # First row contains a 0
        fc = False # First col contains a 0
        for col in range(n):
            if matrix[0][col] == 0:
                fr = True
                break
                
        for row in range(m):
            if matrix[row][0] == 0:
                fc = True
                break
                
        # Use the first row to mark the columns containing 0
        # Use the first col to mark the rows containing 0
        for row in range(1, m):
            for col in range(1, n):
                if matrix[row][col] == 0:
                    matrix[row][0] = 0
                    matrix[0][col] = 0
                    
        # Set the zeros
        for row in range(1, m):
            if matrix[row][0] == 0:
                for col in range(1, n):
                    matrix[row][col] = 0
                    
        for col in range(1, n):
            if matrix[0][col] == 0:
                for row in range(1, m):
                    matrix[row][col] = 0
                    
        if fr:
            for col in range(n):
                matrix[0][col] = 0
        if fc:
            for row in range(m):
                matrix[row][0] = 0
                
        return

class Solution:
    # @param {integer[][]} matrix
    # @return {void} Do not return anything, modify matrix in-place instead.
    def rotate(self, matrix):
        n = len(matrix)
        d = n / 2
        if n % 2 == 0: # n is an even number
            for i in range(d):
                for j in range(d):
                    k = n-1-i
                    l = n-1-j
                    (matrix[j][k], matrix[k][l], matrix[l][i], matrix[i][j]) = (matrix[i][j], matrix[j][k], matrix[k][l], matrix[l][i]) 
        else:
            for i in range(d + 1):
                for j in range(d):
                    k = n-1-i
                    l = n-1-j
                    (matrix[j][k], matrix[k][l], matrix[l][i], matrix[i][j]) = (matrix[i][j], matrix[j][k], matrix[k][l], matrix[l][i])
                    
        return

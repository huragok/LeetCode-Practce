class Solution:
    # @param {integer} n
    # @return {integer[][]}
    def generateMatrix(self, n):
        if n <= 0:
            return [[]]
            
        matrix = [[0] * n for i in range(n)]
        L = 0
        R = n - 1
        T = 0
        B = n - 1
        n_lt = 1
        edge_len = n - 1
       
        for k in range((n + 1) / 2):
            self.circle(matrix, L, R, T, B, n_lt)
            n_lt += 4 * edge_len
            L += 1
            R -= 1
            T += 1
            B -= 1
            edge_len -= 2
            
        return matrix
    
    # Set the values in a circle determined by L, R, B, T, in which the left-top value equals n_lt
    def circle(self, matrix, L, R, T, B, n_lt):
        if L == R:
            matrix[L][T] = n_lt
        else:
            n = n_lt
            for col in range(L, R):
                matrix[T][col] = n
                n += 1
            for row in range(T, B):
                matrix[row][R] = n
                n += 1
            for col in range(R, L, -1):
                matrix[B][col] = n
                n += 1
            for row in range(B, T, -1):
                matrix[row][L] = n
                n += 1
        return

if __name__ == "__main__":
    print(Solution().generateMatrix(0))

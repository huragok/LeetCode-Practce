class Solution:
    # @param {integer[][]} matrix
    # @return {integer[]}
    def spiralOrder(self, matrix):
        m = len(matrix)
        if m == 0:
            return []
        n = len(matrix[0])
        
        # The coordinate of the 4 current circles
        L = 0
        R = n - 1
        T = 0
        B = m - 1
        
        result = []
        while R >= L and B >= T:
            result += self.circle(matrix, L, R, T, B)
            R -= 1
            L += 1
            B -= 1
            T += 1
            
        return result
            
    def circle(self, matrix, L, R, T, B):
        c = [matrix[T][col] for col in range(L, R + 1)] + [matrix[row][R] for row in range(T + 1, B + 1)]
        if B > T:
            c += [matrix[B][col] for col in range(R - 1, L - 1, -1)]
            
        if R > L:
            c += [matrix[row][L] for row in range(B - 1, T, -1)]
        return c
        
if __name__ == "__main__":
    matrix = [
 [ 1, 2, 3, 4],
 [ 5, 6, 7, 8],
 [ 9, 10, 11, 12]
]
    print(Solution().spiralOrder(matrix))
            

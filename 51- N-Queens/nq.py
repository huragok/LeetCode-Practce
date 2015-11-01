class Solution:
    # @param {integer} n
    # @return {string[][]}
    def solveNQueens(self, n):
        emptyboard = ['*' * n] * n 
        return self._solveNQueens(emptyboard, 0, n)
        
    # The function to find all solutions by starting to place queens starting from the i_row-th row on the chess board
    # @param {string[]} chessboard a n-by-n board, partially solved solution, the grid where queens are already placed is marked with 'Q', vulnerable to attack '.', and empty '*'
    # @param {integer} i_row which row to place the next queen
    # @param {integer} n size of the board
    # @return {string[][]}
    def _solveNQueens(self, chessboard, i_row, n):
        if i_row == n - 1: # We are already at the last row, can directly tell whether there are solutions or not
            solutions = []
            for j in range(n):
                if chessboard[i_row][j] == '*':
                    sol = chessboard[:]                    
                    sol[i_row] = '.' * j + 'Q' + '.' * (n - j - 1)
                    solutions.append(sol)
                    
        else: # Not at the last row, need to try all options at the current row and go on recursively
            solutions = []
            for j in range(n):
                if chessboard[i_row][j] == '*':
                    sol_partial = chessboard[:]
                    sol_partial[i_row] = sol_partial[i_row][0:j] + 'Q' + sol_partial[i_row][j+1:]
                    
                    for k in range(n): # The same row is vulnerable
                        if k != j:
                            sol_partial[i_row] = sol_partial[i_row][0:k] + '.' + sol_partial[i_row][k+1:]
                            
                    for step in range(1, n - i_row): # The same column and the same diagonals are vulnerable
                        sol_partial[i_row + step] = sol_partial[i_row + step][0:j] + '.' + sol_partial[i_row + step][j+1:]
                        
                        if j + step < n:
                            sol_partial[i_row + step] = sol_partial[i_row + step][0:j + step] + '.' + sol_partial[i_row + step][j + step+1:]
                            
                        if j - step >= 0:
                            sol_partial[i_row + step] = sol_partial[i_row + step][0:j - step] + '.' + sol_partial[i_row + step][j - step+1:]
                            
                    solutions += self._solveNQueens(sol_partial, i_row + 1, n)
                    
        return solutions
        
if __name__ == "__main__":
    n = 5
    print(Solution().solveNQueens(n))
                        
                            
        
        
    

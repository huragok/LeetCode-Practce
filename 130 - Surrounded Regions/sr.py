class Solution:
    # @param {character[][]} board
    # @return {void} Do not return anything, modify board in-place instead.
    def solve(self, board):
        m = len(board)
        if m <= 0:
            return
        n = len(board[0])
        
        if m <= 2 or n <= 2: # Nothing could possibly be surrounded
            return
        
        # Modified the board in place: replace all 'O' with 'U'.
        for row in range(m):
            for col in range(n):
                if board[row][col] == 'O':
                    board[row][col] = 'U'
        
        # 'X' or 'U' represent unvisited, 'Q' represent added to the queue, 'O' represent all its neighbors has been searched and this position is not surrounded for sure.
        q = [] # The queue of position tuples for the BFS
        
        # Add the initial positions: the "O"s that is on the boundary
        for col in range(n): # The top row and the bottom row
            if board[0][col] == 'U':
                q.append((0, col))
                board[0][col] = 'Q'
                
            if board[m - 1][col] == 'U':
                q.append((m - 1, col))
                board[m - 1][col] = 'Q'
                
        for row in range(1, m - 1): # The left and the right column
            if board[row][0] == 'U':
                q.append((row, 0))
                board[row][0] = 'Q'
                
            if board[row][n - 1] == 'U':
                q.append((row, n - 1))
                board[row][n - 1] = 'Q'
                
        # Start the BFS search
        while q:
            row, col = q.pop(0)
            board[row][col] = 'O'
            if row > 0 and board[row - 1][col] == 'U': # up
                q.append((row - 1, col))
                board[row - 1][col] = 'Q'
            if row < m - 1 and board[row + 1][col] == 'U': # down
                q.append((row + 1, col))
                board[row + 1][col] = 'Q'
            if col > 0 and board[row][col - 1] == 'U': # left
                q.append((row, col - 1))
                board[row][col - 1] = 'Q'
            if col < n - 1 and board[row][col + 1] == 'U': # right
                q.append((row, col + 1))
                board[row][col + 1] = 'Q'
                
        # The positions that are still 'U' are surrounded
        for row in range(m):
            for col in range(n):
                if board[row][col] == 'U':
                    board[row][col] = 'X'
                    
        return
        
if __name__ == "__main__":
    board = [['X', 'X', 'X', 'X'], ['X', 'O', 'O', 'X'], ['X', 'X', 'O', 'X'], ['X', 'O', 'X', 'X']]
    Solution().solve(board)
    print(board)

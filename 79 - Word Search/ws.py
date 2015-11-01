class Solution:
    # @param {character[][]} board
    # @param {string} word
    # @return {boolean}
    def exist(self, board, word):
        m = len(board)
        n = len(board[0])
        board_state = [False] * (m * n)
        
        for row in range(m):
            for col in range(n):
                if self._exist(board, word, board_state, [row, col], m, n):
                    return True
                    
        return False
        
    def _exist(self, board, word, board_state, start, m, n):
        #print("________________________________________")
        #print(board_state)
        #print(start)
        #print(word)
    # Start search from a given start point and given the board_state(whether occupied or not)
        l = len(word)
        if l == 0: # An empty word, return true
            return True
        elif word[0] != board[start[0]][start[1]] or board_state[start[0] * n + start[1]]: # The first letter of the word doesn't match the start point or the starting point has been occupied
            return False
        else:
            board_state[start[0] * n + start[1]] = True # Copy and modify the board state
            neighbors = [] # The neighbors starting from which to search the rest of the word
            if start[0] > 0: # Up neighbor
                neighbors.append([start[0] - 1, start[1]])
            if start[0] < m - 1: # Down neighbor
                neighbors.append([start[0] + 1, start[1]])
            if start[1] > 0: # Left neighbor
                neighbors.append([start[0], start[1] - 1])
            if start[1] < n - 1: # Right neighbor
                neighbors.append([start[0], start[1] + 1])

            for neighbor in neighbors:
                if self._exist(board, word[1:], board_state, neighbor, m, n):
                    return True
            board_state[start[0] * n + start[1]] = False
            if l > 1:       
                return False
            else:
                return True
            
if __name__ == "__main__":
    board = ["ABCE", "SFCS", "ADEE"]
    word = "ABCCED"
    #board = ["a"]
    #word = "a"
    print(Solution().exist(board, word))

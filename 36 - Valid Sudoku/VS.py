class Solution:
    # @param {character[][]} board
    # @return {boolean}
    def isValidSudoku(self, board):
        board_dict = {"1": 0, "2": 1, "3": 2, "4": 3, "5": 4, "6": 5, "7": 6, "8": 7, "9": 8, '.': 9}
        
        top = range(9) + [0] * 9 + [0] * 3 + [3] * 3 + [6] * 3
        bottom = range(9) + [8] * 9 + [2] * 3 + [5] * 3 + [8] * 3
        left = [0] * 9 + range(9) + range(0, 7, 3) * 3
        right = [8] * 9 + range(9) + range(2, 9, 3) * 3
        #print(top)
        return all([isValidCell(board, top[i], bottom[i], left[i], right[i], board_dict) for i in range(27)])
    


def isValidCell(board, top, bottom, left, right, board_dict):
# Verify that whether the cells in board[top : bottom + 1, left : right + 1] contains unique values from "1" ~ "9" other than "."
    count = [0] * 10
    for row in range(top, bottom + 1):
        for col in range(left, right + 1):
            idx = board_dict[board[row][col]]
            if idx < 9 and count[idx] > 0:
                return False
            else:
                count[idx] += 1
            
    return True
            
if __name__ == "__main__":
    board = [".87654321","2........","3........","4........","5........","6........","7........","8........","9........"]
    print(Solution().isValidSudoku(board))
    
    
    

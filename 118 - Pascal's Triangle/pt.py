class Solution:
    # @param {integer} numRows
    # @return {integer[][]}
    def generate(self, numRows):
        output = []
        if numRows < 1:
            return output
        output.append([1])
        
        len_prev_level = 1
        for row in range(1, numRows):
            level = [1]
            level_prev = output[-1]
            for col in range(row - 1):
                level.append(level_prev[col] + level_prev[col + 1])
            level.append(1)
            output.append(level)
            
        return output
        
if __name__ == "__main__":
    print(Solution().generate(5))

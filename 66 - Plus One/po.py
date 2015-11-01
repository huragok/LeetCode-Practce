class Solution:
    # @param {integer[]} digits
    # @return {integer[]}
    def plusOne(self, digits):
        n = len(digits)
        idx = n - 1
        while digits[idx] == 9:
            digits[idx] = 0
            idx -= 1
            
        if idx == -1:
            digits.insert(0, 1)
        else:
            digits[idx] += 1
            
        return digits
        
if __name__ == "__main__":
    digits = [9, 9, 9, 9]
    print(Solution().plusOne(digits))
            

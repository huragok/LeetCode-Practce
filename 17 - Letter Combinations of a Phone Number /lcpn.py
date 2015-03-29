#!/usr/bin/env python

class Solution:
    # @return a list of strings, [s1, s2]
    def letterCombinations(self, digits):
        if not digits:
            return []
        digit2letter = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl','6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
        digit2letter_n = {key: len(val) for key, val in digit2letter.items()}
        
        idx_s = {digit: 0 for digit in digits}
        n_digits = len(digits)
        combi = []
        idxs = [0] * n_digits
        n_combi = 1 # Number of combinations
        for digit in digits:
            n_combi *= digit2letter_n[digit]

        for i_combi in range(n_combi):
            str_tmp = ''.join([digit2letter[digits[i_digit]][idxs[i_digit]] for i_digit in range(n_digits)])
            combi.append(str_tmp)
            #update the idx_s
            for i_digit in range(n_digits - 1, -1, -1):
                if idxs[i_digit] + 1 < digit2letter_n[digits[i_digit]]:
                    idxs[i_digit] += 1
                    break
                else:
                    idxs[i_digit] = 0
        
        return combi

if __name__ == "__main__":
    sol = Solution()
    #digits = '23'
    digits = '5'
    print(sol.letterCombinations(digits))

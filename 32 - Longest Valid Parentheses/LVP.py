#!/usr/bin/env python

class Solution:
    # @param {string} s
    # @return {integer}
    def longestValidParentheses(self, s):
        n = len(s) # Length of the string
        if n <= 1:
            return 0

        max_len_end = [0] * n # The length of the longest substring ending in i
        max_len = 0 # The maximum length currently found 
        stack = 0 # Depth of the parenthesis stack
        for i in range(0, n):
            if s[i] == "(": # push stack
                stack += 1
            else: # pop stack if stack is not empty
                if stack > 0:
                    stack -= 1
                    max_len_end[i] = max_len_end[i-1] + 2 # one more pair of parenthesis than the previous solution

                    # Check if we can concatenate with previous solutions due to the new pair of parenthesis
                    if i - max_len_end[i] >= 0:
                        max_len_end[i] += max_len_end[i - max_len_end[i]]
                    print(max_len_end)
                    max_len = max([max_len, max_len_end[i]]) # Update the maximum length

        return max_len
if __name__ == "__main__":
    s = "()"
    out = Solution().longestValidParentheses(s)
    print(out)
                
                

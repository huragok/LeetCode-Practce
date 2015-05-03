class Solution:
    # @param {string} s
    # @return {boolean}
    def isValid(self, s):
        left = ('(', '[', '{')
        right = (')', ']', '}')
        match = {left[idx]: right[idx] for idx in range(3)}
        stack = list()
        for c in s:
            if c in left:
                stack.append(c)
            elif c in right:
                if len(stack) == 0 or c != match[stack.pop()]:
                    return False
        if len(stack) != 0:
            return False
        else:
            return True
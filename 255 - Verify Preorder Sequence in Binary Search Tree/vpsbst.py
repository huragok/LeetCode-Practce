class Solution(object):
    def verifyPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: bool
        """
        stack = []
        min_leftup = None
        for num in preorder:
            while stack and num > stack[-1]:
                min_leftup = stack.pop()
            if num < min_leftup:
                return False
            stack.append(num)
            
        for idx in xrange(1, len(stack)):
            if stack[idx] > stack[idx - 1]:
                return False
        return True

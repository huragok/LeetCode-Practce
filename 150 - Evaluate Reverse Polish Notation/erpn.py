import operator

class Solution:
    # @param {string[]} tokens
    # @return {integer}
    def evalRPN(self, tokens):
        n = len(tokens)
        if n == 0:
            return None
         
        op = {'+', '-', '*', '/'}
        stack = []
        for t in tokens:
            if t == '+':
                op_right = stack.pop(-1)
                op_left =  stack.pop(-1)
                stack.append(op_left + op_right)
            elif t == '-':
                op_right = stack.pop(-1)
                op_left =  stack.pop(-1)
                stack.append(op_left - op_right)
            elif t == '*':
                op_right = stack.pop(-1)
                op_left =  stack.pop(-1)
                stack.append(op_left * op_right)
            elif t == '/':
                op_right = stack.pop(-1)
                op_left =  stack.pop(-1)
                stack.append(int(operator.truediv(op_left, op_right)))
            else:
                stack.append(int(t))
        return stack[-1]
        
if __name__ == "__main__":
    tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
    print(Solution().evalRPN(tokens))

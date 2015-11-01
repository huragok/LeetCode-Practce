class Solution:
    # @param {integer} n
    # @param {integer} k
    # @return {string}
    def getPermutation(self, n, k):
        
        factorials = [1]
        min_fct = 0 # the smallest value such that min_fct! >= k
        while factorials[0] < k:
            min_fct += 1
            factorials.insert(0, factorials[0] * min_fct)
        #min_fct -= 1
        factorials.pop(0)
        
        result = range(1, n - min_fct + 1)
        digits = range(n - min_fct + 1, n + 1)
        res = k
        print(min_fct)
        print(result)
        #print(digits)
        print(factorials)
        i_factorial = 0
        for pos in range(n - min_fct + 1, n + 1):
            order = (res - 1) / factorials[i_factorial]
            print("________")
            print(digits)
            print((res, order))
            print(result)
            result.append(digits.pop(order))
            res -= order * factorials[i_factorial]
            i_factorial += 1
            
        return ''.join(map(str, result))
        
                
        
if __name__ == "__main__":
    n = 4
    k = 24
    print(Solution().getPermutation(n, k))
        
        
        
        

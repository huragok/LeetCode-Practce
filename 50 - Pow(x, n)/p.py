class Solution:
    # @param {float} x
    # @param {integer} n
    # @return {float}
    def myPow(self, x, n):
        if n == 0:
            return 1.0
        elif n < 0:
            x = 1 / x
            n = -n
            
        pow_partial = [1, x] # pow_partial[n] = x ** n
        
        pow_tmp = x
        p_max_floor = 1
        sub = 2
        while sub <= n:
            sub *= 2
            p_max_floor += 1
            pow_tmp = pow_tmp * pow_tmp
            pow_partial.append(pow_tmp)
        
        res = n
        result = 1
        while res > 0:
            p = 0 # Try to find the maximum power that is smaller than or equal to the current residual
            sub = 1
            while sub <= res:
                sub *= 2
                p += 1
                
            res -= sub / 2
            result *= pow_partial[p]
        return result
        
if __name__ == "__main__":
    x = 34.00515
    n = -3
    print(Solution().myPow(x, n))        
        
        
    

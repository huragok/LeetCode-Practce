class Solution:
    # @param {integer} numerator
    # @param {integer} denominator
    # @return {string}
    def fractionToDecimal(self, numerator, denominator):
        output = ""
        if numerator * denominator < 0:
            output += "-"
        
        numerator = numerator if numerator >=0 else -numerator
        denominator = denominator if denominator >=0 else -denominator
        
        integ = numerator / denominator
        output += str(integ)
        residual = numerator - integ * denominator
        
        frac = ""
        res_to_pos = dict() # Residual to position
        pos = 0
        flag_loop = False
        while residual > 0:
            if residual in res_to_pos:
                flag_loop = True
                pos_first = res_to_pos[residual]
                break
            
            digit = residual * 10 / denominator
            frac += str(digit)
            res_to_pos[residual] = pos
            residual = (residual * 10) % denominator
            pos += 1
            
            
        if pos == 0:
            return output
        elif not flag_loop:
            return output + "." + frac
        else:            
            return output + "." + frac[0:pos_first] + '(' + frac[pos_first:] + ')'
            
if __name__ == "__main__":
    numerator = 1
    denominator = 99
    print(Solution().fractionToDecimal(numerator, denominator))

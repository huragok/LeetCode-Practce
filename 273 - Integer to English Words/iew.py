class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return 'Zero'

        result = ''
        
        billion = num / 1000000000
        num -=  billion * 1000000000
        if billion > 0:
            result += self._numberToWords(billion) + ' Billion'
            if num > 0:
                result += ' '
                
        million = num / 1000000
        num -= million * 1000000
        if million > 0:
            result += self._numberToWords(million) + ' Million'
            if num > 0:
                result += ' '
                
        thousand = num / 1000
        num -= thousand * 1000
        if thousand > 0:
            result += self._numberToWords(thousand) + ' Thousand'
            if num > 0:
                result += ' '
        result += self._numberToWords(num)
        
        return result
        
    def _numberToWords(self, num):
        # num must be less in [0, 999], here 0 returns ''
        dict0 = {0: '', 1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', 6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine'}
        dict10 = {10: 'Ten', 11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen', 15: 'Fifteen', 16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen', 19: 'Nineteen'}
        dict20 = {20: 'Twenty', 30: 'Thirty', 40: 'Forty', 50: 'Fifty', 60: 'Sixty', 70: 'Seventy', 80: 'Eighty', 90: 'Ninety'}
        
        h = num / 100
        td = num - h * 100
        result = ''
        if h > 0:
            result += dict0[h] + ' Hundred'
            if td > 0:
                result += ' '
        if 0 <= td <= 9:
            result += dict0[td]
        elif 10 <= td <= 19:
            result += dict10[td]
        elif td >= 20:
            t = td / 10
            d = td - t * 10
            if d > 0:
                result += dict20[t * 10] + ' ' + dict0[d]
            else:
                result += dict20[t * 10]
        return result
            
            
if __name__ == "__main__":
    num = 0
    print(Solution().numberToWords(num))

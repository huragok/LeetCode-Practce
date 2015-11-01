import collections

class Solution(object):
    def generatePalindromes(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        count = collections.defaultdict(int)
        for c in s:
            count[c] += 1
            
        center = [c for c in count if count[c] % 2 == 1]
        if len(center) > 1:
            return []
        count_half = {c: count[c] / 2 for c in count if count[c] / 2 > 0}
        #print(count_half)
        self.half = []
        self.generateFirstHalf(count_half, '', sum(count_half.values()))
        #print(self.half)
        
        if not center:
            return [h + h[-1::-1] for h in self.half]
        else:
            return [h + center[0] + h[-1::-1] for h in self.half]
        
    def generateFirstHalf(self, count_half, partial_half, n):

        if n == 0:
            self.half.append(partial_half)
        else:
            for c in count_half:
                if count_half[c] > 0:
                    count_half[c] -= 1
                    self.generateFirstHalf(count_half, partial_half + c, n - 1)
                    count_half[c] += 1
  
                    
if __name__ == "__main__":
    s = "abc"
    print(Solution().generatePalindromes(s))

import collections

class Solution(object):
    def groupStrings(self, strings):
        """
        :type strings: List[str]
        :rtype: List[List[str]]
        """
        self.pos = {letter: idx for idx, letter in enumerate('abcdefghijklmnopqrstuvwxyz')}
        sigs = collections.defaultdict(list)
        for string in strings:
            sigs[self.getSignature(string)].append(string)
            
        return sigs.values()
        
    def getSignature(self, string):
        n = len(string)
        if n == 0:
            return None
        elif n == 1:
            return tuple()
        else:
            signature = [None] * (n - 1)
            for idx in range(1, n):
                signature[idx - 1] = (self.pos[string[idx]] - self.pos[string[idx - 1]]) % 26
            return tuple(signature)
            
if __name__ == "__main__":
    strings = ["aa", "bb", 'b']
    print(Solution().groupStrings(strings))

class Solution:
    # @param {string} a
    # @param {string} b
    # @return {string}
    def addBinary(self, a, b):
        return "{0:b}".format(int(a, 2) + int(b, 2))
        
if __name__ == "__main__":
    a = '11'
    b = '1'
    print(Solution().addBinary(a, b))
        
        

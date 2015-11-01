import itertools

class Solution:
    # @param {string} version1
    # @param {string} version2
    # @return {integer}
    def compareVersion(self, version1, version2):
        list1 = str(version1).split('.')
        list2 = str(version2).split('.')
        for s1, s2 in itertools.izip_longest(list1, list2):
            if s1 == None:
                if int(s2) == 0:
                    return 0
                else:
                    return -1
            elif s2 == None:
                if int(s1) == 0:
                    return 0
                else:
                    return 1
            elif int(s1) > int(s2):
                return 1
            elif int(s1) < int(s2):
                return -1
                
        return 0
        
if __name__ == "__main__":
    version1 = 1
    version2 = 1.12
    print(Solution().compareVersion(version1, version2))

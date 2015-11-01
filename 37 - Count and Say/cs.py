class Solution:
    # @param {integer} n
    # @return {string}
    def countAndSay(self, n):
        map_say = {'11': '21', '12': '11', '21': '12', '22': '22'}
        map_step = {'11': 2, '12': 1, '21': 1, '22': 2}   

        if n < 1:
            return ''
        seq = '1'
        for i in range(1, n):
            seq = say(seq, map_say, map_step)

        return seq
 
  
def say(s, map_say, map_step):
# The function to read a string: 1 become 11, 11 become 21
    n = len(s) # Length of the string
    if n < 1:
        return ''
    
    ptr = 0
    
    s_say = ''
    while ptr < n:
        count = 0
        val = s[ptr]
        while ptr + count < n and s[ptr + count] == val:
            count += 1
        ptr += count
        s_say += str(count) + str(val)
            
    return s_say
    
if __name__ == "__main__":
    seq = Solution().countAndSay(20)
    print(seq)

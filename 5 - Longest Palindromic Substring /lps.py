#!/usr/bin/env python3

class Solution:
    # @return a string
    def longestPalindrome(self, s):
        l = len(s)
        max_length = 0
        max_center = 0
        flag_odd = True
        
        for center in range(l + 1):
            # odd symmetry
            for radius in range(1, min((center + 1, l - center)) + 1):
                if s[center + radius - 1] != s[center - radius + 1]:
                    radius -= 1
                    break

            if 2 * radius  - 1 > max_length:
                max_length = 2 * radius - 1
                max_center = center
                flag_odd = True

        for center_left in range(l):
            # even symmetry
            for radius in range(1, min((center_left + 1, l - center_left- 1)) + 1):
                if s[center_left - radius + 1] != s[center_left + radius]:
                    radius -= 1
                    break
            if 2 * radius > max_length:
                max_length = 2 * radius
                max_center = center_left
                flag_odd = False
                    
        if flag_odd:
            max_radius = max_length // 2 + 1 
            palindrome = s[max_center - max_radius + 1 : max_center + max_radius]
        else:
            max_radius = max_length // 2
            palindrome = s[max_center - max_radius + 1 : max_center + max_radius + 1]

        return palindrome

if __name__ == "__main__":
    s = "wasitacatisaw123"
    p = Solution().longestPalindrome(s)
    print("s = {0}".format(s))
    print("p = {0}".format(p))

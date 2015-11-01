class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        origin = x
        reverse = 0
        while x > 0:
            reverse = reverse * 10 + x % 10
            x /= 10
        print(reverse)
        return reverse == origin


if __name__ == "__main__":
    x= 12321
    print(Solution().isPalindrome(x))

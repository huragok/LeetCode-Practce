# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
# def read4(buf):

class Solution:
    # @param buf, Destination buffer (a list of characters)
    # @param n,   Maximum number of characters to read (an integer)
    # @return     The number of characters read (an integer)
    def read(self, buf, n):
        count = 0
        buf4 = [""] * 4
        while count < n:
            c = read4(buf4)
            for idx in range(min([c, n - count])):
                buf[count + idx] = buf4[idx]
            count += c
            if c < 4:
                break
        return min([count, n])

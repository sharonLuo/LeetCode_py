

# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
# def read4(buf):

class Solution(object):
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """
        buffer = [""]*4
        length = 0
        while length+4<=n:
            cur_len = read4(buffer)
            for i in range(cur_len):
                buf[length+i] = buffer[i]
            length += cur_len
            if cur_len<4:
                break
        
        if length<n<length+4:
            cur_len = read4(buffer)
            add = min(n-length, cur_len)
            for i in range(add):
                buf[length+i] = buffer[i]
            length += add
        return length


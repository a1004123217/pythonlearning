class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 0:
            sign = -1
        else:
            sign = 1
        rst = int(str(abs(x))[::-1])
        rst = rst * sign
        if(rst >= 2 ** 31 or rst <= -2 ** 31):
            return 0;
        else:
            return rst

test = Solution()
while(1):
    tmp = int(input())
    print(test.reverse(tmp))
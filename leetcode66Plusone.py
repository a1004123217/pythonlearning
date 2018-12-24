class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        digits[len(digits)-1] += 1
        lend = len(digits)-1
        while lend >= 0:
            if digits[lend] == 10:
                digits[lend] = 0
                if lend - 1 < 0:
                    digits.insert(0, 1)
                else:
                    digits[lend - 1] += 1
                lend -= 1
            elif digits[lend] < 10:
                break
        return digits
x = Solution()
print(x.plusOne([9]))
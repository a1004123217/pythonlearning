class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        l,substring = 0,''
        for c in s:
            if c in substring:
                substring = substring.split(c)[-1]
            substring += c
            if len(substring)>l:
                l = len(substring)
        return(l)



test = Solution()
while True:
     x = input()
     print(test.lengthOfLongestSubstring(x))
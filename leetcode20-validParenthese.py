class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        dicmap = {0: None, "{":"}", "(":")","[":"]"}
        stack = [0]
        for element in s:
            if element in dicmap:
                stack.append(element)
            else:
                if dicmap[stack.pop()] != element:
                    return False
        return stack == [0]
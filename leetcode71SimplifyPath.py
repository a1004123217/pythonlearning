class Solution:
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        place = [p for p in path.split("/") if p is not "." and p is not ""]
        stack = []
        for s in place:
            if s == "..":
                if len(stack) > 0:
                    stack.pop()
            else:
                stack.append(s)
        return "/" + "/".join(stack)
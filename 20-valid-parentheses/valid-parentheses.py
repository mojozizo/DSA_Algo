class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        HashMap = { '}': '{', ']': '[', ')': '(' }

        for i in s:
            if i in HashMap:
                if stack and HashMap[i] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)

        return True if not stack else False
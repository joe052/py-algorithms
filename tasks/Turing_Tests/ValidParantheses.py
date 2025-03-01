class Solution:
    def isValid(self, s):
        dct = {'(': ')', '{': '}', '[': ']'}
        stack = []
        l = len(s)
        if l == 0:
            return True
        if l % 2 != 0:
            return False
        for num, char in enumerate(s):
            if char in dct:
                stack.append(dct[char])
            elif stack and char == stack[-1]:
                stack.pop(-1)
            else:
                return False
        return not stack
´´´

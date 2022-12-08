class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) < 2 or len(s) % 2 != 0: return False
        pars = {"(":")",
                "{":"}",
                "[":"]"}
        if s[0] not in pars: return False
        to_close = [pars[s[0]]]
        for i in range(1,len(s)):
            if s[i] in pars: 
                to_close.append(pars[s[i]])
            elif s[i] == to_close[-1]:
                to_close.pop()
            else:
                return False
        return to_close == []

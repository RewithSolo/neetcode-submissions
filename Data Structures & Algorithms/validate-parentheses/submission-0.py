class Solution(object):
    def isValid(self, s):
        stack = []
        dict_brackets = {")":"(", "}":"{", "]":"["}
        for i in range(len(s)):
            if s[i] in dict_brackets:
                if not stack:
                    return False
                
                if stack[-1] == dict_brackets[s[i]]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(s[i])
        
        if stack:
            return False
        
        return True
        
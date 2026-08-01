class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        matching = {')': '(', ']': '[', '}': '{'}
        for i in range(len(s)):
            if s[i] in '({[' :
                stack.append(s[i])
            else:
                if len(stack)==0:
                    return False
                elif stack.pop() != matching[s[i]]:
                    return False
        return len(stack) == 0
        
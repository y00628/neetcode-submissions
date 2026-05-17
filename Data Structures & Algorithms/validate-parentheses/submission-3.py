from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False

        push = {'{', '(', '['}
        pop = {'}', ')', ']'}
        pairs = {'{}', '()', '[]'}

        stack = deque([])

        for c in s:
            if c in push:
                stack.append(c)
            elif len(stack) == 0 and c in pop:
                return False
            elif stack.pop() + c not in pairs:
                return False
            
        return len(stack) == 0



class Solution:
    def isValid(self, s: str) -> bool:

        open_brakets = {
            '(' : ')',
            '[' : ']',
            '{' : '}',
        }

        close_brakets = {
            '}' : '{',
            ')' : '(',
            ']' : '[',
        }

        stack = []

        for c in s:
            if c in open_brakets:
                stack.append(c)
            elif c in close_brakets and stack:
                prev = stack.pop()
                if close_brakets[c] != prev:
                    return False
            else:
                return False

        return not stack;
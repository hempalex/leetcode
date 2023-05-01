class Solution:
    def myAtoi(self, s: str) -> int:

        s = s.lstrip()

        negative = False
        if s and (s[0] == '-' or s[0] == '+'):
            if s[0] == '-':
                negative = True
            s = s[1:]

        num = 0
        for c in s:
            if c.isdigit():
                num = num * 10 + (ord(c) - ord('0'))
            else:
                break
                
        if negative:
            num = -num
    
        num = max(-2**31, min(num, 2**31 - 1))

        return num
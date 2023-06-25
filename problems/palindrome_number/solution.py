class Solution:
    def isPalindrome(self, x: int) -> bool:

        if x < 0: return False

        p = 0
        y = x

        while y:
            p = p * 10 + (y % 10) #
            y = y // 10

        return p == x


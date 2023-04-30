class Solution:
    def isSameAfterReversals(self, num: int) -> bool:

        return self.reverse(self.reverse(num)) == num

    def reverse(self, x: int) -> int:
        sign = 1
        if (x < 0):
            sign = -1
            x = -x

        r = 0
        while x != 0:
            d = x % 10
            r = r * 10 + d
            x //= 10

        if r >= 2 ** 31 - 1:
            return 0

        return r*sign
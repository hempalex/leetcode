class Solution:
    def reverseBits(self, n: int) -> int:

        r = 0
        for i in range(32):
            bit = (n >> i) & 0x1
            r = (r << 1) | bit

        return r

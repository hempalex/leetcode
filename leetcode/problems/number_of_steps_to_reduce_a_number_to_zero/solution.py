class Solution:
    def numberOfSteps(self, num: int) -> int:
        steps = 0
        while num > 0:
            steps = steps + (1 if num % 2 == 0 or num == 1 else 2)
            num = num >> 1
        return steps

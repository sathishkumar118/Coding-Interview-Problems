class Solution:
    def __init__(self):
        self._dict = {1: 1, 2: 2}
    def climbStairs(self, n: int) -> int:
        if n not in self._dict.keys():
            self._dict[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
        return self._dict[n]
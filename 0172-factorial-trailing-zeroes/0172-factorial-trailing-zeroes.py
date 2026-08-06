class Solution:
    def trailingZeroes(self, n: int) -> int:
        c = 0
        i = 1
        while (5**i<=n):
            c+=n//5**i
            i+=1
        return c
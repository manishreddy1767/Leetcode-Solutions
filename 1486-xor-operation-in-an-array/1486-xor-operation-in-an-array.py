class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        x = 0
        for i in range(start,start+n*2,2):
            x^=i
        return x
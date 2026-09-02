class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        s = 0
        p = 1
        while n:
            rem = n%10
            n = n//10
            s+=rem
            p*=rem
        return p-s
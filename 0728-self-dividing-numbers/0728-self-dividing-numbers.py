class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        l = []
        for i in range(left, right + 1):
            n = i
            valid = True
            while n:
                rem = n % 10
                if rem == 0 or i % rem != 0:
                    valid = False
                    break
                n //= 10
            if valid:
                l.append(i)
        return l

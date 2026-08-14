class Solution:
    def canJump(self, nums: List[int]) -> bool:
        c = 0
        for n in nums:
            if c < 0:
                return False
            elif n > c:
                c = n
            c -= 1
            
        return True
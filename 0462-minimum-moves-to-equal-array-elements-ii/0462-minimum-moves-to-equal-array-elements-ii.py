class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        nums.sort()
        a = nums[len(nums)//2]
        c = 0
        for i in nums:
            c+=abs(i-a)
        return c
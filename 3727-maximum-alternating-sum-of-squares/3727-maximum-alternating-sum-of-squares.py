class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        s = 0
        n = len(nums)
        for i in range(n):
            nums[i]=abs(nums[i])
        nums.sort()
        for i in range(n//2):
            s -= nums[i]*nums[i]
        for i in range(n//2,n):
            s += nums[i]*nums[i]
        return s
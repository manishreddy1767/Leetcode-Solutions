class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        prefmax = [-float("inf")] * n
        suffmin = [float("inf")] * n
        prefmax[0] = nums[0]
        suffmin[-1] = nums[-1]
        for i in range(1, n):
            prefmax[i] = max(nums[i], prefmax[i - 1])
        for i in range(n - 2, -1, -1):
            suffmin[i] = min(nums[i], suffmin[i + 1])
        for i in range(n):
            if prefmax[i] - suffmin[i] <= k:
                return i
        return -1
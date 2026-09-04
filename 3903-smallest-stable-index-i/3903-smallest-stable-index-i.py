class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        res=float('inf')
        n=len(nums)
        for i in range(n):
            max_val=max(nums[:i+1])
            min_val=min(nums[i:])
            if (max_val-min_val) <=k:
                res=min(res,i)
        if res == float('inf'):
            return -1
        else:
            return res             
            
        
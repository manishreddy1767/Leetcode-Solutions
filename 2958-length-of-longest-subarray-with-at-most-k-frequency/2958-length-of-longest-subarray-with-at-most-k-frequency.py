class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        l=0
        n=len(nums)
        d={}
        violators=0 
        for r in range(n):
            if nums[r] not in d:
                d[nums[r]]=0
            d[nums[r]]+=1
            if d[nums[r]]>k:
                violators+=1
            if violators>0:
                d[nums[l]]-=1
                if d[nums[l]]>=k:
                    violators-=1
                l+=1      
        return r-l+1
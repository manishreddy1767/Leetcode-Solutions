class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        n = len(nums)
        d = {}
        for i in nums:
            d[i]=d.get(i,0)+1
        for i,j in d.items():
            if j>=n//2:
                return i
        return -1

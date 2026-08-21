class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        d = {}
        for i in nums:
            d[i] = d.get(i,0)+1
        c = 0
        for i in d.values():
            c+=i*(i-1)//2
        return c
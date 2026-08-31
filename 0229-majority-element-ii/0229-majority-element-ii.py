class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        d = {}
        for i in nums:
            d[i]=d.get(i,0)+1
        x = len(nums)//3
        l=[]
        for i,j in d.items():
            if j>x:
                l.append(i)
        return l
        
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        e = [i for i in nums if i%2==0]
        o = [i for i in nums if i%2!=0]
        return e+o
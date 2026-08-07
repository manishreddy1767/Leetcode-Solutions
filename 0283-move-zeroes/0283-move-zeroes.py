class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        n = len(nums)
        k = 0
        
        for i in range(n):
            if nums[i] != 0:
                nums[k], nums[i] = nums[i], nums[k]
                k += 1
        

                
                
class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        e = [x for x in nums if x % 2 == 0]
        o = [x for x in nums if x % 2 != 0]

        i = 0
        j = 0

        for k in range(len(nums)):
            if k % 2 == 0:
                nums[k] = e[i]
                i += 1
            else:
                nums[k] = o[j]
                j += 1

        return nums
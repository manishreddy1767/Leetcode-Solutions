class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        n = len(nums)

        for i in range(n - 1):
            for j in range(n - i - 1):
                x = str(nums[j])
                y = str(nums[j + 1])

                if x + y < y + x:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]

        ans = "".join(map(str, nums))
        return "0" if ans[0] == "0" else ans
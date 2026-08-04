class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        m = float("inf")
        nums.sort()
        n = len(nums)

        for i in range(n - 2):
            j = i + 1
            k = n - 1

            while j < k:
                s = nums[i] + nums[j] + nums[k]

                if m > abs(target - s):
                    x = s
                    m = abs(target - s)

                if s > target:
                    k -= 1
                elif s < target:
                    j += 1
                else:
                    return target

        return x
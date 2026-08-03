class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n = len(nums1)
        m = len(nums2)

        i = j = 0
        prev = curr = 0

        for _ in range((n + m) // 2 + 1):
            prev = curr

            if i < n and (j >= m or nums1[i] <= nums2[j]):
                curr = nums1[i]
                i += 1
            else:
                curr = nums2[j]
                j += 1

        if (n + m) % 2 == 0:
            return (prev + curr) / 2
        else:
            return curr
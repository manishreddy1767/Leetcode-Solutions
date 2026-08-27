from collections import Counter
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        c = Counter(nums1)
        l=[]
        for i in nums2:
            if c[i]>0:
                l.append(i)
                c[i]-=1
        return l

        
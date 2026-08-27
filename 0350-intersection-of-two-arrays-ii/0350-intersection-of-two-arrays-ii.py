from collections import Counter
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        c1 = Counter(nums1)
        c2 = Counter(nums2)
        l=[]
        for i,j in c1.items():
            if i in c2:
                for x in range(min(j,c2[i])):
                    l.append(i)
        return l

        
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        l = []
        for i in range(k):
            m = max(c,key=c.get)
            l.append(m)
            del c[m]
        return l
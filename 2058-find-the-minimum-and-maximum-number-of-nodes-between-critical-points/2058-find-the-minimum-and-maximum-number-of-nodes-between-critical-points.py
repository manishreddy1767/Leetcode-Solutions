class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        c = 1
        l = []
        temp = head
        prev = None
        nex = temp.next
        while nex and nex.next:
            prev = temp
            temp = temp.next
            nex = nex.next
            c += 1
            if (temp.val > prev.val and temp.val > nex.val) or \
               (temp.val < prev.val and temp.val < nex.val):
                l.append(c)
        if len(l) < 2:
            return [-1, -1]
        min_dist = min(l[i] - l[i-1] for i in range(1, len(l)))
        max_dist = l[-1] - l[0]
        return [min_dist, max_dist]
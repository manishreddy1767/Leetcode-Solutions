class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        restore = [""] * len(indices)
        for i in range(len(indices)):
            restore[indices[i]] = s[i]
        return "".join(restore)
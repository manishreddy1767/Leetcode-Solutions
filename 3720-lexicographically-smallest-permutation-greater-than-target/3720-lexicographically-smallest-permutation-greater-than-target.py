class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        s = "".join(sorted(s, reverse=True))
        ans = ""
        for i, x in enumerate(target):
            if x in s:
                s_temp = s.replace(target[i], "", 1)
                if s_temp > target[i+1:]:
                    ans += target[i]
                    s = s_temp
                    continue

            s = "".join(sorted(s))
            for y in s:
                if y > target[i]:
                    s_temp = s.replace(y, "", 1)
                    ans += y
                    ans += s_temp
                    break
            break
        return ans
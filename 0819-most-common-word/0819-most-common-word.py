from collections import defaultdict

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        word_list = re.findall(r'\b\w+\b', paragraph.lower())
        hashmap = defaultdict(int)
        for each in word_list:
            if each not in banned:
                hashmap[each] = hashmap[each] + 1
        return max(hashmap, key=hashmap.get)
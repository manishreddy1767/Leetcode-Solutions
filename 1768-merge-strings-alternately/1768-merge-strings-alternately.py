class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = 0
        j = 0
        x=""
        while i<len(word1) and j<len(word2):
            x+=word1[i]
            x+=word2[i]
            i+=1
            j+=1
        while i<len(word1):
            x+=word1[i]
            i+=1
        while j<len(word2):
            x+=word2[j]
            j+=1
        return x
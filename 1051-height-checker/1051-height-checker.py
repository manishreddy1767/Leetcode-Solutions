class Solution:
    def heightChecker(self, arr):
        n = len(arr)
        freq = []
        counter = Counter(arr)
        for i in range(max(arr)+1):
            freq.append(counter[i])
        #position array
        pos = [freq[0]]
        for i in range(1, len(freq)):
            pos.append(pos[i-1] + freq[i])

        #sorted array
        sor = [0] * n
        for num in arr:
            sor[pos[num]-1] = num
            pos[num] -= 1

        #answer question
        res = 0
        for i in range(len(sor)):
            if sor[i] != arr[i]: res += 1
        return res
            
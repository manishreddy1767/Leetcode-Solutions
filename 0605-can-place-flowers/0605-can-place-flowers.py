class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if len(flowerbed) == 1:
            if flowerbed[0] == 0:
                n -= 1
            return n <= 0
        for i in range(len(flowerbed) - 1):
            if i == 0 and not flowerbed[i] and not flowerbed[i + 1]:
                flowerbed[i] = 1
                n -= 1
            elif i != 0:
                if not flowerbed[i - 1] and not flowerbed[i] and not flowerbed[i + 1]:
                    flowerbed[i] = 1
                    n -= 1
        if not flowerbed[-1] and not flowerbed[-2]:
            flowerbed[-1] = 1
            n -= 1
        return n <= 0
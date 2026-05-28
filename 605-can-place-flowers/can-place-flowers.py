"""
ok so if n flowers can be planted
ok so we can check like the amount of things that dont have an adjacent plot, but that will change, sooo....

we can try to just place stuff and see if we run out of n

0 0 0 0 1 0 0
"""

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0: return True
        if len(flowerbed) == 1:
            return not flowerbed[0]
        for i in range(len(flowerbed)):
            if flowerbed[i] != 1:

                if i == 0:
                    if flowerbed[i + 1] != 1:
                        flowerbed[i] = 1 
                        n-=1
                elif i == len(flowerbed)-1:
                    if flowerbed[i - 1] != 1:
                        flowerbed[i] = 1 
                        n-=1
                elif flowerbed[i-1] !=1 and flowerbed[i+1] != 1:
                    flowerbed[i] = 1
                    n-=1

        print(flowerbed)
        return n <= 0
"""
ok so the sum of both has to be at least success?

all are positive


ok so we return something of len(spells), 

we can search for potions such as spells[i] * potion[j] > success

we can use brute force and that's O(m x n)

if we sort one and start popping it's overall O(mxn + nlogn) in the worst case

i mean we need to get something >= (success / spell),

so if we sort and then do a binary search, 

O(m + nlogn)

ok so if we sort potions, then search and get the ones that are at least...

O(mlogn + nlogn)

ok it's importan that it is confirmed that spells and potions are
"""
class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        res = []

        m = len(potions)
        max_potion = potions[m - 1]

        for spell in spells:
            min_potion = success / spell
            if min_potion > max_potion:
                res.append(0)
                continue
            i = bisect.bisect_left(potions, min_potion)
            res.append(m - i)
        return res
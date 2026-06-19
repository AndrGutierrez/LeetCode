from collections import Counter
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        appearances = Counter(arr)
        existing = set()
        for ap in appearances.values():
            if ap in existing: return False
            else: existing.add(ap)
        return True
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        aux = [c for c in sorted(citations) if c!=0]
        h=len(aux)
        for i, amount in enumerate(aux):
            if amount >= len(aux[i:]):
                h=min(len(aux[i:]), amount)
                return h
        return h
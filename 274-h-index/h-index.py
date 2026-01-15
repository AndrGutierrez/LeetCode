class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        aux = [0]*(n+1)
        for c in citations:
            if c>=n: c=n
            aux[c]+=1
        k=n
        s=aux[n]
        while k> s:
            k-=1
            s+=aux[k]
        return k
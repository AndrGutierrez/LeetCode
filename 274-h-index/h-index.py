class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        aux = [0]*(n+1)
        for c in citations:
            aux[min(c,n)]+=1
        k=n
        s=aux[n]
        print(aux)
        while k> s:
            print(k, s, aux[k])
            k-=1
            s+=aux[k]
        return k
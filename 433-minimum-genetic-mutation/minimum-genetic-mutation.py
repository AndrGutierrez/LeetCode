"""
if they didnt have to be in the bank the solution would be just the diff

creating all the mutations and checking if theyre in the bank is probably a lot... just 4 characters tho, 

but if we connect all the genes that have a diff of 1, and then make a linked list...

not linked list because there might be more, just a graph connecting to all, and then calculate the shortest path


"""

from collections import deque
class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        graph = defaultdict(list)
        bank.append(startGene)
        for gene in bank:
            for possible_neighbor in bank:
                diff =0
                for (c1, c2) in zip(gene, possible_neighbor):
                    if c1 != c2:
                        diff+=1
                if diff==1:
                    graph[gene].append(possible_neighbor)
        q = deque([startGene])
        distances = {
            node: None for node in bank
        }
        distances[startGene]=0
        q=deque([startGene])
        while q:
            current_node = q.popleft()
            for neighbor in graph[current_node]:
                # print(neighbor)

                if distances[neighbor] is None:
                    distance = distances[current_node]+1
                    distances[neighbor] = distance
                    q.append(neighbor)
        distances.setdefault(endGene, -1)
        if distances[endGene] is None: distances[endGene] = -1
        return distances[endGene]
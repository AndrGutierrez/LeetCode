"""
adjacent pair of words (adjacency list?)

beginword doesnt need to be in wordlist (starting node?)

each word differs by a single letter

shortest transformation sequence

each one differs one but not necessarily linear

so, build the graph with each one and find the shortest path, dont see much more complication than that

time complexity sfhouldnt be a problem, can be more than O(n2) in the worst case probably

traverse the array for each element and if it differs in one word add to adjacency list, cycles dont seem to be a problem in bfs

the way to set neighbors needs to be different but how

loa
lob
loc
lod
"""

from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        graph = defaultdict(list)
        distances = defaultdict(int)
        fullList = wordList
        if wordList[0] != beginWord: fullList = [beginWord] + wordList
            
      
        for i in range(len(fullList)):
            word = fullList[i]
            for j in range(i, len(fullList)):
                word2 = fullList[j]
                if i != j:
                    diff_amount = 0
                    for k in range(len(word)):
                        if word[k] != word2[k]: diff_amount+=1
                        if diff_amount > 1: break
                    if diff_amount == 1: 
                        graph[word].append(word2)
                        graph[word2].append(word)
                    # if diff_amount >1: break
        
        q = deque([beginWord])
        visited = set([beginWord])
        steps = 0
        res = None
        distances[beginWord] = 1
        while q and not res:
            node = q.popleft()

            for neighbor in graph[node]:
                if neighbor not in visited:
                    q.append(neighbor)
                    visited.add(neighbor)
                    distance = distances[node]+1
                    distances[neighbor]= distance
                    if neighbor == endWord: 
                        res = distances[neighbor]
                        break
        if not res: return 0
        return res
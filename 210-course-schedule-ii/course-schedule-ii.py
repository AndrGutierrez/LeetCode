"""
num of courses is smaller than before so we might be able to sort
idk

all pairs are unique

courses we should finish in order

there might be more than one correct solution(?)

i think is the same as last but we add each node to a response array and thats it

because first we put the ones with no requirements, 

if impossible return empty array

so, topological order sort, and save it, though 

ok just assume that if theres n courses just assume they're all named from 0 to n-1
"""
from collections import deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        in_degree = defaultdict(int)
        graph = defaultdict(list[int])
        for i in range(numCourses):
            in_degree[i]+=0
        for course, prerequisite in prerequisites:
            in_degree[course] +=1

            graph[prerequisite].append(course)
        
        q = deque()
        res = []
        for course in in_degree.keys():
            if in_degree[course] == 0:
                q.append(course)
        while q:
            node = q.popleft()
            res.append(node)
            neighbors = graph[node]
            for neighbor in neighbors:
                in_degree[neighbor] -=1
                if in_degree[neighbor] == 0:
                    q.append(neighbor)
        if len(res) == numCourses:
            return res
        else: return []
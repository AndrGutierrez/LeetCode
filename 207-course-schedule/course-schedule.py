"""
cursos

return if i can finish all the courses

bfs isn it?

if the amount doesnt equal the amount of courses return false

ok but first make the graph, then bfs

so the problem is where do i start i guess, if i start from last course
thats a problem, should i sort it?

i'll sort it first and then check if it can be optimized

well first of all its a directed graphs so...

is this djikstra?

like its an infinite cost unless we coursed the prerequisite

if not specified, the course doesnt have a prerequisite, so we should start by the one without prerequisites and do bfs from there, there might be more 
than one without prerequisites so make sure to handle that

pairs are unique

check the ones without prerequisites,

then, go to each one and 

if you make a matrix

"""
from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(set)
        in_degree = [0]*numCourses
        q = deque()
        coursed = 0


        for (course, prerequisite) in prerequisites:
            graph[prerequisite].add(course)
            in_degree[course] +=1

        for i in range(numCourses):
            if in_degree[i] ==0:
                q.append(i)
            

        while q:
            node = q.popleft()
            coursed+=1
            neighbors = graph[node]
            for neighbor in neighbors:
                    in_degree[neighbor] -=1
                    if in_degree[neighbor] == 0:
                        q.append(neighbor)
        return coursed >= numCourses

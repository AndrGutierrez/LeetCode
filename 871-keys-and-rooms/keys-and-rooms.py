"""
ok so I think we can do either bfs or dfs the thing is visiting all nodes, there might be cicles like

[[1],[0]] so we gotta keep a list of visited nodes

i think we can do it recursively but iterating too, like go to this one, keep going to children until the q is empty, and then go to next
"""
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        rooms_to_visit = set(list(range(1, len(rooms))))
        visited = set()
        q =  deque(list(rooms[0]))
        while q:
            room = q.pop()
            if room not in visited:
                visited.add(room)
                rooms_to_visit.discard(room)

                for neighbor in rooms[room]:
                    q.append(neighbor)
        return len(rooms_to_visit) == 0


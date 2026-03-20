"""
find the equations system, save each equation into a hashmap so you could recalculate each time or save

but like if you find something there...  theres multiplication so...

no, anyway if you find a variable that is not in the hashmap theres no solution

forget it, theres multiple terms so...

ok this is marked as graph

so the wird thing here is division

max for each equation is 5 terms, though there might be digits in them

solve the equation... saving into hashmap might take several operations...


despeje->save into hashmap...

no theres gotta be something easier

a - 2b = 0
b - 3c = 0

systems of equations might be undetermined, so that doesnt work

but if we do something like

ab -> 2
bc -> 3

ba -> (ab)^-1
ac -> (a/b)(b/c) cancels out
aa -> a/b* a/b^-1

but thats logical, you either way find an algorithm that does that or look for other approach

can I use a hashmap? doesnt seem to
can I use divide and conquer? probably not
can I use a graph? lets model this as a tree

2
a, b

3
b, c
"""
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(defaultdict)

        def backtrack_evaluate(curr_node, target_node, acc_product, visited):
            visited.add(curr_node)
            ret  = -1.0
            neighbors = graph[curr_node]
            if target_node in neighbors:
                ret = acc_product * neighbors[target_node]
            else:
                for neighbor, value in neighbors.items():
                    if neighbor in visited:
                        continue
                    ret = backtrack_evaluate(
                        neighbor, target_node, acc_product * value, visited
                    )
                    if ret != -1.0:
                        break
            visited.remove(curr_node)
            return ret

        for (dividend, divisor), value in zip(equations, values):
            graph[dividend][divisor] = value
            graph[divisor][dividend] = 1/value

        results = []

        for dividend, divisor in queries:
            if dividend not in graph or divisor not in graph:
                ret = -1.0

            elif dividend == divisor:
                ret = 1.0
            
            else:
                visited = set()
                ret = backtrack_evaluate(dividend, divisor, 1, visited)
            results.append(ret)
        return results
        
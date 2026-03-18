"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
looks like bfs

max 100 nodes

no loops
all nodes are connected

go to next,

it has a node with 1 as default

if you traverse the array, the val of the node is i (i starts from 1), and
the neighbors are arr[i-1] 

add val, and create the neighbors

save the neighbors into a hashmap

if a node is in the hashmap just add the neighbors
"""
import copy
from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        return copy.deepcopy(node)
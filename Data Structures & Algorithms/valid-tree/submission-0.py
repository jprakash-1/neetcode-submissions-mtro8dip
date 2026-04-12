from collections import defaultdict
from typing import List

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n:
            return True

        adj = defaultdict(list)
        for i, j in edges:
            adj[i].append(j)
            adj[j].append(i)

        visited = set()

        def dfs(i, prev):
            if i in visited:
                return False

            visited.add(i)

            for node in adj[i]:
                if node != prev:
                    if not dfs(node, i):
                        return False

            return True

        return dfs(0, -1) and n == len(visited)
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        def dfs(i, c):
            if color[i] != 0:
                if color[i] != c:
                    return False
                return True
            color[i] = c
            for v in graph[i]:
                if not dfs(v, 3 - c):
                    return False
            return True
             
        n = len(graph)
        color = [0] * n
        for i in range(n):
            if color[i] == 0:
                if not dfs(i, 1):
                    return False
        return True
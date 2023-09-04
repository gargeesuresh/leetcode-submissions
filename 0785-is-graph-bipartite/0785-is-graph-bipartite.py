class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        
        def dfs(node,color):
            if visited[node]>0:
                if visited[node]!=color:
                    return False
                return True
            else:
                visited[node]=color
                for nei in graph[node]:
                    if not dfs(nei,3-color):
                        return False
            return True
    
        n=len(graph)
        visited = [0]* n
        
        
        for i in range(n):
            if visited[i]==0:
                if not dfs(i,1):
                    return False

        return True
    
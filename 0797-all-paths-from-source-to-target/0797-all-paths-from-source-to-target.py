class Solution:
    
    def dfs(self,graph,node,path,paths):
        
        
        if node==(len(graph)-1):
            paths.append([int(x) for x in path.split(",")])
            return 
        
        for val in graph[node]:
            
            self.dfs(graph,val,path+","+str(val),paths)
                
        
            
    
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        
        
        paths=[]
        path="0"
        self.dfs(graph,0,path,paths)
        return paths
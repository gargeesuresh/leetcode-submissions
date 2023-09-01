class Solution:
    
    def dfs(self,visited,edge_list,node):
        visited[node]=True
        
        for i in edge_list[node]:
            if visited[i]==False:
                self.dfs(visited,edge_list,i)        
        return 
                    
    def canReach(self, arr: List[int], start: int) -> bool:
        # 0 -> 4
        # 1 -> 3
        # 2 -> 5
        # 3 ->
        # 4 -> 1
        # 5 -> 4, 6
        # 6 -> 4
        
        zero_indexes=[]              
        visited=[False]*len(arr)
        
        edge_list=[[] for i in range(len(arr))]
        for ind,val in enumerate(arr):
            if val==0:
                zero_indexes.append(ind)
                continue
            if ind-arr[ind]>=0:
                edge_list[ind].append(ind-val)
            if ind+val<len(arr):
                edge_list[ind].append(ind+val)
        
        self.dfs(visited,edge_list,start)
        
        for ind in zero_indexes:
            if visited[ind]:
                return True
        
        return False

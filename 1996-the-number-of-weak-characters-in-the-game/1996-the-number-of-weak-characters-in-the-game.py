class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        d = defaultdict(list)
        for atk, dfn in properties:
            d[atk].append(dfn)
            
        weak, max_dfn = 0, -1
        for k in sorted(d.keys(), reverse=True):
            for dfn in d[k]:
                if dfn < max_dfn: 
                    weak += 1
                    
            max_dfn = max(max_dfn, max(d[k]))
                
        return weak
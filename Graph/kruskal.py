from collections import defaultdict
import heapq
class Solution:
#**********************************************************************************************************
#                                         Krushkal's Algo
#**********************************************************************************************************
    def spanningTree(self, V, adj):
        edges=[]
        for i in range(len(adj)):
            for j,c in adj[i]:
                edges.append((c,i,j))
                
        edges.sort()      
       
        cost=0
        
        parent=[i for i in range(len(adj))]
        
        def find(a):
            if a==parent[a]:
                return a
            parent[a]=find(parent[a])
            return parent[a]
            
        for c,u,v in edges:
            p1=find(u)
            p2=find(v)
            if p1!=p2:
                cost+=c
                parent[p2]=p1
    
        return cost
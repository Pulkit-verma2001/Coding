from collections import defaultdict
import heapq
class Solution:
    
    #Function to find sum of weights of edges of the Minimum Spanning Tree.
    def spanningTree(self, V, adj):
        graph=defaultdict(list)
        for i in range(len(adj)):
            for j,c in adj[i]:
                graph[i].append((j,c))
                graph[j].append((i,c))
        
        distance=[float('inf')]*V
        parent=[-1]*V
        mst=[False]*V
        distance[0]=0
        heap=[(0,0)]
        while len(heap):
            c,node=heapq.heappop(heap)
            if mst[node]==True : continue
            mst[node]=True
            for nei,co in graph[node]:
                if mst[nei]==False and distance[nei]>co:
                    distance[nei]=co
                    parent[nei]=node
                    heapq.heappush(heap,(co,nei))
        
        return sum(distance)
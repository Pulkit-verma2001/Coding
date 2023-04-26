from collections import defaultdict
import heapq
class Solution:
    def dijkstra(self, V, adj, S):
        graph=defaultdict(list)
        for i in range(len(adj)):
            for j in range(len(adj[i])):
                graph[i].append((adj[i][j][0],adj[i][j][1]))
            
        distance=[float('inf')]*V
        visited=[False]*V
        heap=[(0,S)]
        distance[S]=0
        visited[S]=0
        while len(heap):
            c,n=heapq.heappop(heap)
            if visited[n] : continue
            visited[n]=True
            for neigh in graph[n]:
                node,dis=neigh
                new_dis=c+dis
                if distance[node]>new_dis:
                    distance[node]=new_dis
                    heapq.heappush(heap,(new_dis,node))
        return distance
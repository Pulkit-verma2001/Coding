
class Solution:
    # Function to construct and return cost of MST for a graph
    # represented using adjacency matrix representation
    '''
    V: nodes in graph
    edges: adjacency list for the graph
    S: Source
    '''
    def bellman_ford(self, V, edges, S):
        dis=[int(1e8)]*V
        dis[S]=0
        
        for i in range(V-1):
            for edge in edges:
                u=edge[0]
                v=edge[1]
                wt=edge[2]
                
                if dis[u]!=int(1e8) and dis[u]+wt<dis[v]:
                    dis[v]=dis[u]+wt
        
        for u,v,wt in edges: # for checking negative Edge Cycle, 
                             #If Dis array get updated in Nth iteration 
                             #it indicate there is negative edge in graph
            if dis[u]!=float('inf') and dis[u]+wt<dis[v]:
                return [-1]
        return dis

class Solution:
    def topoSort(self, V, adj):
        inDegree=[0]*V
        for i in range(V):
            for n in adj[i]:
                inDegree[n]+=1
        queue=[]
        for i in range(V):
            if inDegree[i]==0:
                queue.append(i) # pushing the node whose indegree is 0
        topo=[]
        while len(queue):
            node=queue.pop(0)
            topo.append(node)
            for ne in adj[node]:
                inDegree[ne]-=1 # decreasing indegree of node because 
                                # we have explore one of the node that was involved in its indegree
                if inDegree[ne]==0 :
                    queue.append(ne)
        return topo
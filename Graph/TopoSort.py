class Solution:
    
    #Function to return list containing vertices in Topological order.
    def topoSort(self, V, adj):
        def dfs(node,stack):
            visited[node]=1
            for ne in adj[node]:
                if visited[ne]==0:
                    dfs(ne,stack)      
            stack.append(node)
        stack=[]
        visited=[0]*V
        for i in range(V):
            if visited[i]!=1:
                dfs(i,stack)

        return stack[::-1]

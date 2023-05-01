class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        parent=[i for i in range(len(points))]

        def find(a):
            if a==parent[a] : return a
            parent[a]=find(parent[a])
            return parent[a]
        
        edges=[] # making edges by leting point(i) to be node i
        for i in range(len(points)):
            for j in range(i,len(points)):
                v1,v2=points[i]
                u1,u2=points[j]
                dis=abs(u1-v1)+abs(u2-v2)
                edges.append((dis,i,j))
        edges.sort() # sort the array on basis of ditance between two nodes
        
        cost=0
        
        for d,u,v in edges:
            pu=find(u)
            pv=find(v)
            if pu!=pv: # if parent not same means they are in different components
                cost+=d
                parent[pv]=pu # merge both node in single components
        return cost
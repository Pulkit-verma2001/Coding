class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n=len(isConnected)
        p=[i for i in range(n)]
        def find(a):
            if a==p[a]:
                return a
            p[a]=find(p[a])
            return p[a]
        def union(a,b):
            p1=find(a)
            p2=find(b)
            if p1!=p2:
                p[p2]=p1
        for i in range(n):
            for j in range(n):
                if isConnected[i][j]==1:
                    union(i,j)
        ans=0
        for i in range(n):
            if p[i]==i:
                ans+=1
        return ans
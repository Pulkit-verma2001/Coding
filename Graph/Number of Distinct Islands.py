class Solution:
    def countDistinctIslands(self, grid : List[List[int]]) -> int:
        directions=[(1,0),(-1,0),(0,1),(0,-1)]
        def dfs(row,col,vis,lst,bRow,bCol):
            vis[row][col]=1
            lst.append((row-bRow,col-bCol)) 
            for x,y in directions:
                nrow,ncol=row+x,col+y
                if nrow>=0 and nrow<n and ncol>=0 and ncol<m and vis[nrow][ncol]==0 and grid[nrow][ncol]==1:
                    dfs(nrow,ncol,vis,lst,bRow,bCol)
        
        
        
        n=len(grid)
        m=len(grid[0])
        
        vis=[[0 for _ in range(m)] for _ in range(n)]
        st=set()
        for i in range(n):
            for j in range(m):
                if vis[i][j]==0 and grid[i][j]==1:
                    lst=[]
                    dfs(i,j,vis,lst,i,j)
                    st.add(tuple(lst))
        return len(st)
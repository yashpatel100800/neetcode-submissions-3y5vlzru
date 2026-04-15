class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        n = len(grid)
        m = len(grid[0])

        
        int_max = 2147483647
        q = deque()
        dr = [0,1,0,-1]
        dc = [1,0,-1,0]
        
        def bfs(r,c,d):
            q.append([r,c,d])

            while q:
                row, col, dist = q.popleft()
                for i in range(4):
                    nr = row + dr[i]
                    nc = col + dc[i]
                    if(nr>=0 and nr<n and nc>=0 and nc<m and grid[nr][nc]>dist+1):
                        grid[nr][nc] = dist+1
                        bfs(nr,nc,dist+1)



        for i in range(n):
            for j in range(m):
                if (grid[i][j] == 0):
                    bfs(i,j,0)

        print(grid)
        

class Solution {
public:

    void dfs(int i, int j, vector<vector<char>>& grid, vector<vector<int>>& visited){
        int m = grid.size();
        int n = grid[0].size();        
        visited[i][j] = 1;
        int dr[] = {0,1,0,-1};
        int dc[] = {1,0,-1,0};
        for(int k=0;k<4;k++){
            int nr = i+dr[k];
            int nc = j+dc[k];
            if(nr<m && nr>=0 && nc<n && nc>=0 && visited[nr][nc] != 1 && grid[nr][nc] == '1'){
                dfs(nr,nc,grid, visited);
            }
        }

    
    }

    int numIslands(vector<vector<char>>& grid) {
        int count = 0;
        int m = grid.size();
        int n = grid[0].size();
        vector<vector<int>> visited(m, vector<int>(n,0));

        for(int i = 0; i<m; i++){
            for(int j = 0; j<n; j++){
                if(grid[i][j] == '1' && visited[i][j] == 0){
                    count++;
                    dfs(i, j, grid, visited);
                }
            }
        }

        return count;
    }
};

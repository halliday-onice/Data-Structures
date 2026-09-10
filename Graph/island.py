#leetcode 200
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        visited = set()
        def dfs(row, col):
            if row < 0 or col < 0 or row >= rows or col >= cols:
                return 
            if grid[row][col] == "0":
                return
            
            if (row, col) in visited: #se eu ja visitei o item do grid, desisto
                return
            
            #se chegou ate aqui to vivo ainda, entao adiciona ao visited
            visited.add((row, col))

            dfs(row + 1, col)
            dfs(row, col + 1) 
            dfs(row - 1, col)
            dfs(row, col - 1)
                

             #visited.remove((row, col)) nao

            
        

        island_count = 0
        for i in range(rows):
            for j in range(cols):
                #run the dfs - quando nao tiver visitado e for 1, e
                if grid[i][j] == "1" and (i, j) not in visited:
                   island_count += 1
                   dfs(i, j)

        return island_count
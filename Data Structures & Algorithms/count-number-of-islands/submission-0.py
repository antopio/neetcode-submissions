class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        count = 0
        for r in range(len(grid)):
            for c in range(len(grid[r])):

                if grid[r][c] == "1":
                    count += 1
                    self.bfs(grid, r, c)

        return count 


    def bfs(self, grid, r, c):
        queue = deque([(r,c)])
        grid[r][c] = "0" # visited
        while queue:
            len_queue = len(queue)
            for i in range(len_queue):
                row, col = queue.popleft()
                directions = [(-1,0),(1,0),(0,1),(0,-1)]
                for dr, dc in directions:
                    new_r, new_c = row + dr, col + dc
                    # check if new_r and new_c are not out of bounds.
                    if 0 <= new_r < len(grid) and 0 <= new_c < len(grid[0]):
                        if grid[new_r][new_c] == "1":

                            grid[new_r][new_c] = "0"
                            queue.append((new_r, new_c))


                



        



from collections import deque


class Solution:
    def islandPerimeter(self, grid) -> int:
        if not grid:
            return 0

        q = deque([])
        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        delimeter = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    q.append([i, j])

                    while q:
                        x, y = q.popleft()
                        grid[x][y] = -1

                        for d in dirs:
                            new_x = x + d[0]
                            new_y = y + d[1]

                            cell = self.determine_cell(grid, new_x, new_y)
                            if cell == 1:
                                q.append([new_x, new_y])
                                grid[new_x][new_y] = -1
                            elif cell == 0:
                                delimeter += 1

                    break

        return delimeter

    def determine_cell(self, grid, x, y):
        """
        0: water
        1: land
        2: visited or out
        """
        if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or grid[x][y] == 0:
            return 0

        return 1 if grid[x][y] == 1 else -1

#     def calc_water_sides(self, grid, x, y):
#         if grid[x][y] != 1:
#             return 0

#         water_sides = 0

#         if x == 0 or (x > 0 and grid[x-1][y]) == 0:
#             water_sides += 1

#         if x == len(grid) - 1 or (x < len(grid) - 1 and grid[x+1][y]) == 0:
#             water_sides += 1

#         if y == 0 or (y > 0 and grid[x][y-1]) == 0:
#             water_sides += 1

#         if y == len(grid[0]) - 1 or (y < len(grid[0]) - 1 and grid[x][y+1]) == 0:
#             water_sides += 1

#         return water_sides

s = Solution()
grid = [[1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1]]
grid = [[0,0,0,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,1,1,1,1,1,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,1,1,1,1,1,1,0,1,0,1,1,0],[0,0,0,0,0,0,0,0,0,1,1,1,1,0,0,1,0,0,1,0],[0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,0,0,1,0],[0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],[0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],[0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0],[1,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],[1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],[0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],[0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],[0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],[0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0],[0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0],[0,0,1,1,1,0,1,1,1,1,1,1,1,1,1,1,0,0,0,0],[0,0,1,1,1,0,1,1,1,1,1,1,0,0,1,1,0,0,0,0],[0,0,1,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0],[0,0,1,1,0,0,0,0,1,1,1,1,1,0,0,0,0,0,0,0]]
print(s.islandPerimeter(grid))
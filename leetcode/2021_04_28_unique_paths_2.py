class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        n_rows = len(obstacleGrid)
        n_cols = len(obstacleGrid[0])
        paths_grid = [[0] * n_cols for _ in range(n_rows)]

        if obstacleGrid[0][0] == 1:
            return 0

        paths_grid[0][0] = 1
        for row in range(n_rows):
            for col in range(n_cols):
                curr_paths = 0
                if obstacleGrid[row][col] == 1:
                    continue
                if row >= 1:
                    curr_paths += paths_grid[row - 1][col]
                if col >= 1:
                    curr_paths += paths_grid[row][col - 1]
                paths_grid[row][col] += curr_paths

        return paths_grid[row][col]


if __name__ == "__main__":
    sol = Solution()
    print(sol.uniquePathsWithObstacles([[0, 0, 0], [0, 1, 0], [0, 0, 0]]))

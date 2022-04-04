'''
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3

TestCases:
[["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]
[["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
[["1","1","0","0"],["0","0","1","0"],["1","0","0","0"]]
[["1","0"]]
[["1"]]
[["0"]]

'''

class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        count = 0
        for i in range(0,len(grid)):
            for j in range(0,len(grid[0])):
                if grid[i][j] == '1':
                    count += 1
                    self.visit_island(i,j,grid)
        return count
    
    def visit_island(self,i,j,grid):
        if i < 0 or j < 0 or i == len(grid) or j == len(grid[0]) or grid[i][j] != '1':
            return
        else:
            grid[i][j] = '0'
            self.visit_island(i,j+1,grid)
            self.visit_island(i,j-1,grid)
            self.visit_island(i+1,j,grid)
            self.visit_island(i-1,j,grid)
    
    
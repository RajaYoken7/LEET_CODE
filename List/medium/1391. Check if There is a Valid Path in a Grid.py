from typing import List
class UnionFind:
    def __init__(self, m, n):
        self.m, self.n = m, n
        self.root = [i for i in range(m*n)]
        self.size = [1] * (m*n)

    def get_1d_index(self, x, y):
        return (x * self.n) + y

    def find(self, x):
        if x != self.root[x]:
            self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self, r1, c1, r2, c2):
        x, y = self.get_1d_index(r1, c1), self.get_1d_index(r2, c2)
        rootX, rootY = self.find(x), self.find(y)
        if rootX != rootY:
            if self.size[rootX] >= self.size[rootY]:
                self.root[rootY] = rootX
                self.size[rootX] += self.size[rootY]
            else:
                self.root[rootX] = rootY
                self.size[rootY] += self.size[rootX]

class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])
        uf = UnionFind(m, n)
        right_key, down_key = 'right', 'down'
        connections = {
            1: { right_key: set([1, 3, 5]), down_key: set([]) },
            2: { right_key: set([]), down_key: set([2, 5, 6]) },
            3: { right_key: set([]), down_key: set([5, 6, 2]) },
            4: { right_key: set([1, 3, 5]), down_key: set([2, 5, 6]) },
            5: { right_key: set([]), down_key: set([]) },
            6: { right_key: set([1, 3, 5]), down_key: set([]) }
        }

        for i in range(m):
            for j in range(n):
                # Right
                ri, rj = i, j+1
                if rj < n and grid[ri][rj] in connections[grid[i][j]][right_key]:
                    uf.union(i, j, ri, rj)

                # Down
                di, dj = i+1, j
                if di < m and grid[di][dj] in connections[grid[i][j]][down_key]:
                    uf.union(i, j, di, dj)

        return uf.find(uf.get_1d_index(0, 0)) == uf.find(uf.get_1d_index(m-1, n-1))

# Notes:
# - Use Union-Find to connect adjacent cells that have matching pipe openings.
# - Map 2D grid coordinates to a 1D index for the Union-Find data structure.
# - For each cell, check if its right or down neighbor has a compatible pipe to form a connection.
# - Finally, check if the top-left cell (start) is in the same set as the bottom-right cell (end).
#
# Example Walkthrough: 2x2 grid. Start at (0,0).
# If (0,0) connects to (0,1), union them.
# If (0,1) connects to (1,1), union them.
# End check: find(0) == find(3) -> True.
#
# Time Complexity : O(M*N * alpha(M*N))
# Space Complexity: O(M*N) for Union-Find arrays
# Technique       : Union-Find (Disjoint Set)
# Pattern         : Graph Connectivity
        

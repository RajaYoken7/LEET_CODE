from typing import List
class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        r, c=len(box), len(box[0])
        rotate=[['.']*r for _ in range(c)]
        for i, row in enumerate(box):
            bottom=c-1
            for j in range(c-1, -1, -1):
                if row[j]=='#':
                    rotate[bottom][r-1-i]='#'
                    bottom-=1
                elif row[j]=='*':
                    rotate[j][r-1-i]='*'
                    bottom=j-1
        return rotate

# Notes:
# - Simulate gravity for each row independently by moving stones (`#`) to the furthest empty spot (`bottom`).
# - When an obstacle (`*`) is hit, update the `bottom` to be just above the obstacle.
# - Place the processed items directly into their 90-degree rotated positions.
#
# Example Walkthrough: row=["#", ".", "*", "."]
# j=3 (.): bottom=3.
# j=2 (*): place at rotated. bottom=1.
# j=1 (.): bottom=1.
# j=0 (#): place '#' at rotated[bottom].
#
# Time Complexity : O(M * N)
# Space Complexity: O(M * N) for rotated matrix
# Technique       : Two Pointers (Gravity simulation)
# Pattern         : Matrix Rotation / Simulation
        
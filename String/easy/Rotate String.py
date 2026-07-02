class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        # 1. Rotations only work if the lengths are identical
        if len(s) != len(goal):
            return False
            
        # 2. If goal is a rotation of s, it must exist within s + s
        return goal in (s + s)
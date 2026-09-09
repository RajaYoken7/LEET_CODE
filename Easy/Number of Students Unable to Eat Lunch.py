class Solution:
    def countStudents(self, students: list[int], sandwiches: list[int]) -> int:
        # 1. Count how many students want circular (0) and square (1) sandwiches
        from collections import Counter
        count = Counter(students)
        
        # 2. Iterate through the stack of sandwiches
        for sandwich in sandwiches:
            # If there is at least one student who wants this type, they will 
            # eventually reach the front of the queue and take it.
            if count[sandwich] > 0:
                count[sandwich] -= 1
            else:
                # If no one left in the queue wants this sandwich, the 
                # process stops because the stack is blocked.
                break
                
        # 3. The remaining count values are the students who couldn't eat
        return count[0] + count[1]

# Notes:
# - Count the number of students preferring each type of sandwich (0 or 1).
# - Iterate through the sandwich stack. If there is at least one student who wants the top sandwich, they will eventually get it.
# - If no student wants the current top sandwich, the queue is deadlocked and no one else can eat.
#
# Example Walkthrough: students=[1,1,0,0], sandwiches=[0,1,0,1]
# count = {0:2, 1:2}
# sand=0: count[0]>0 -> count={0:1, 1:2}
# sand=1: count[1]>0 -> count={0:1, 1:1}
# sand=0: count[0]>0 -> count={0:0, 1:1}
#
# Time Complexity : O(N)
# Space Complexity: O(1) (counter is size 2)
# Technique       : Counting / Simulation
# Pattern         : Queue Simulation
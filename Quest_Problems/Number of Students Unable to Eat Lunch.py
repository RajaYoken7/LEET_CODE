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
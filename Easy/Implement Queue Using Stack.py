class MyQueue:

    def __init__(self):
        # input_stack: used for push operations
        # output_stack: used for pop/peek operations
        self.in_stack = []
        self.out_stack = []

    def push(self, x: int) -> None:
        # Standard stack push
        self.in_stack.append(x)

    def pop(self) -> int:
        # Ensure out_stack has elements, then pop from it
        self.peek()
        return self.out_stack.pop()

    def peek(self) -> int:
        # If out_stack is empty, move all elements from in_stack to out_stack
        # This reverses the order, making the oldest element the top of out_stack
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
        return self.out_stack[-1]

    def empty(self) -> bool:
        # Queue is empty only if both stacks are empty
        return not self.in_stack and not self.out_stack

# Notes:
# - Use two stacks to simulate a queue: one for pushing (`in_stack`) and one for popping (`out_stack`).
# - Push operation is always O(1) by appending to `in_stack`.
# - Pop/Peek operations require transferring elements from `in_stack` to `out_stack` (reversing order) ONLY when `out_stack` is empty.
#
# Example Walkthrough: push(1), push(2), pop()
# push 1, 2 into in_stack=[1,2].
# pop(): out_stack is empty. move in_stack to out_stack -> out=[2,1].
# pop from out_stack -> returns 1. out=[2].
#
# Time Complexity : Push O(1), Pop/Peek Amortized O(1)
# Space Complexity: O(N)
# Technique       : Two Stacks
# Pattern         : Data Structure Design
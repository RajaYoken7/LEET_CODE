import re

class Solution(object):
    def simplifyPath(self, path):
        tokens = [t for t in path.split('/') if t and t != '.']
        stack = []
        for token in tokens:
            if token == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(token)
        
        return '/' + '/'.join(stack)

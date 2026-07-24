class Solution:
    def simplifyPath(self, path: str) -> str:
        
        stack = []

        paths = path.split('/')

        for word in paths:

            if word == '..':
                if stack:
                    stack.pop()
            elif word != '' and word!= '.':
                stack.append(word)
        
        return '/' + '/'.join(stack)
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []

        for c in tokens:

            if c == "+":
                val2 = stack.pop()
                val1 = stack.pop()

                val = int(val1) + int(val2)

                stack.append(str(val))
            elif c == "-":
                val2 = stack.pop()
                val1 = stack.pop()

                val = int(val1) - int(val2)

                stack.append(str(val))
            elif c == "*":
                val2 = stack.pop()
                val1 = stack.pop()

                val = int(val1) * int(val2)

                stack.append(str(val))
            elif c == "/":
                val2 = int(stack.pop())
                val1 = int(stack.pop())

                val = int(val1 / val2)

                stack.append(str(val))
            else:
                stack.append(c)
        
        return int(stack[-1])
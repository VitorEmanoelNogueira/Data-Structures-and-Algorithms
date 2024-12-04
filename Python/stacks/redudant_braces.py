class Solution:
    def braces (self, A):
        stack =[]

        for c in A:
            if c != ")":
                stack.append(c)
            else:
                count = 0
                while stack[-1] != "(":
                    popped = stack.pop()
                    if popped in "+-*/": 
                        count += 1
                stack.pop()

                if count == 0:
                    return 1
        return 0
class Solution:
    def is_valid(self, s: str) -> bool:
        stack = []

        mapping = {
            "}": "{",
            ")": "(",
            "]": "[" 
        }

        for c in s:
            if c in "([{":
                stack.append(c)
            else:
                if stack and stack[-1] == mapping[c]:
                        stack.pop()
                else:
                    return False
        
        return len(stack) == 0


class Solution:
    def findType(self, s: str):
        if s == '(' or s == ')':
            return "normal"
        elif s == '{' or s == '}':
            return "curvy"
        else:
            return "square"

    def isValid(self, s: str) -> bool:
        stack = []

        for ele in s:
            tp = self.findType(ele)
            if ele == ')' or ele == '}' or ele == ']':
                if len(stack) != 0:
                    if stack[-1] == tp:
                        stack.pop()
                    else:
                        return False
                else:
                    return False
            else:
                stack.append(tp)

        if len(stack) == 0:
            return True
        else:
            return False



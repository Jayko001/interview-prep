class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = []
        stack = []

        for i in range(len(temperatures)):
            stack.append(temperatures[i])

            if temperatures[i] > temperatures[i-1] and i != 0:
                temp = len(stack)
                while stack():
                    stack.pop()
                    result.append(temp)
                    temp -= 1

        return result

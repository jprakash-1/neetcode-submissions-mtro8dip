class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)   # must be pre-sized
        stack = []  # each element: [temp, index]

        for index, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                stackTemp, stackindex = stack.pop()
                res[stackindex] = index - stackindex

            stack.append([temp, index])

        return res

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0]*len(temperatures)

        stack = []
        for index, temperature in enumerate(temperatures): 
            print(stack)
            while stack and stack[-1][-1] < temperature: 
                i, temp = stack.pop()
                res[i] = index - i 

            stack.append((index,temperature))

        return res

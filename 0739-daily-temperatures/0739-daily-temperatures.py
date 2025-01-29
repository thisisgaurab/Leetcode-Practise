class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0]*len(temperatures)
        
        for i, temp in enumerate(temperatures):
            while stack and temp > temperatures[stack[-1]]:
                before_i = stack.pop()
                result[before_i] = i - before_i
            stack.append(i)

        return result
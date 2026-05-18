from collections import deque

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # [38 30 36 35] 1 4 
        # We can use a stack to maintain indices in a 
        # monotonically decreasing order, popping indices where 
        # the values are smaller than the current element. 

        # pop until top element >= curr

        n = len(temperatures)
        answer = [0] * n
        stack = []  # stores indices, monotonically decreasing by temperature

        for i, temp in enumerate(temperatures):
            # Pop all days that are cooler than today
            while stack and temperatures[stack[-1]] < temp:
                prev = stack.pop()
                answer[prev] = i - prev
            stack.append(i)

        return answer
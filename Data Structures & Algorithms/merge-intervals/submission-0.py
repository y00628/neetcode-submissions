class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        if len(intervals) == 1:
            return intervals
        
        intervals.sort(key=lambda x: x[0])
        output = [intervals[0]]

        for i in range(1, len(intervals)):
            start, end = intervals[i]

            if start <= output[-1][1]:
                output[-1][1] = max(end, output[-1][1])
            else: 
                output.append(intervals[i])

        return output


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        if len(intervals) == 0:
            return [newInterval]

        # 1, 2, 4
        # 3, 5, 6

        
        intervals.append(newInterval)
        intervals.sort(key=lambda x: x[0])
        output = [intervals[0]]

        for i in range(1, len(intervals)):
            if intervals[i][0] <= output[-1][1]:
                output[-1][1] = max(output[-1][1], intervals[i][1])
            else:
                output.append(intervals[i])

        return output


        # still sort by start
        # if start <= prev_end, modify last entry of output with [prev_start, max(prev_end, end)]
        # [[1,3],[2,5],[4,6]]]
        # [[1,6]]


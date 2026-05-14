class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if len(intervals) == 1:
            return 0

        erased = 0

        intervals.sort(key=lambda x: x[0])

        prev_start, prev_end = intervals[0]

        # minimum removal = remove larger blocks

        for i in range(1, len(intervals)):
            curr_start, curr_end = intervals[i]

            if curr_start >= prev_end: # non overlapping
                prev_end = curr_end
                continue

            # increment erased, keep earlier end
            erased += 1
            prev_end = min(prev_end, curr_end)

        return erased

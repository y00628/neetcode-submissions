"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:

        n = len(intervals)

        if n <= 1:
            return n

        rooms_needed = 0
        events = []

        for interval in intervals:
            events.append((interval.start, 1))
            events.append((interval.end, 0))

        events.sort(key=lambda x: (x[0], x[1]))
        occupied = 0

        for time, e_type in events:
            if e_type == 1:
                occupied += 1
                rooms_needed = max(rooms_needed, occupied)
            else:
                occupied -= 1

        return rooms_needed
                



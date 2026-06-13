from collections import defaultdict

class TimeMap:

    def __init__(self):
        self.tm = defaultdict(list) # key: [value, timestamp]


    def set(self, key: str, value: str, timestamp: int) -> None:
        self.tm[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        lo, hi = 0, len(self.tm[key]) - 1
        res = -1

        while lo <= hi:
            mid = (lo + hi) // 2
            if self.tm[key][mid][1] <= timestamp:
                res = mid       # valid candidate, but keep searching right
                lo = mid + 1
            else:
                hi = mid - 1

        return "" if res == -1 else self.tm[key][res][0]


                    

class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        # Pair and sort by position descending (closest to target first)
        cars = sorted(zip(position, speed), reverse=True)
        
        stack = []  # tracks arrival times of fleets
        
        for pos, spd in cars:
            time = (target - pos) / spd
            
            # Only push if this car takes LONGER than the car ahead
            # (meaning it can't catch up → forms its own fleet)
            if not stack or time > stack[-1]:
                stack.append(time)
            # If time <= stack[-1], this car catches up to the fleet ahead
            # (it gets absorbed, so we don't push)
        
        return len(stack)
        
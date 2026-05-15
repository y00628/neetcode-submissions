class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        n = len(numbers)

        if n == 2:
            return [1, 2]

        res = []
        first_found = 0
        curr_idx = 0


        # 1st num: normally iterate until comp is found
        # append first idx

        while curr_idx < n:
            curr = numbers[curr_idx]

            if not first_found:
                comp = target - curr

            if (not first_found and comp not in numbers[curr_idx+1:]) or (first_found and curr != comp):
                curr_idx += 1
            elif first_found:
                res.append(curr_idx+1)
                break
            else:
                first_found = 1
                res.append(curr_idx+1)
                curr_idx += 1


        return res
from collections import defaultdict

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        # check +/- 1
        # if no -> new group start from 1 (group index)
        # if yes, check left and right
        #   group[idx] += 1

        # check nums every time
        # if left and right -> del right grp, and update right group_id
        # elif either: group_lead += 1, num[id] = old_group_id 
        # otherwise, startup

        # 2: 4, 20: 1, 10: 1
        # 2: 2, 20: 20, 4: 2, 10: 10, 3: 2, 5: 2

        # Ignore duplicates: If a number is already in your map, skip it.
        # Check Neighbors: Look for num - 1 and num + 1.
        # Calculate Length: The new length of the sequence is left_len + right_len + 1.
        # Update Boundaries: You only need to update the grp_idx for num, num - left_len, and num + right_len.

        if len(nums) <= 1:
            return len(nums)

        grp = defaultdict(int)

        for num in nums:
            if num in grp:
                continue 

            if num-1 in grp and num+1 in grp:
                left, right = grp[num-1], grp[num+1]
                grp[num] = left+1+right
                grp[num-left] = grp[num]
                grp[num+right] = grp[num]
            elif num-1 in grp:
                left = grp[num-1]
                grp[num] = left+1
                grp[num-left] = grp[num] 
            elif num+1 in grp:
                right = grp[num+1]
                grp[num] = 1+right
                grp[num+right] = grp[num] 
            else:
                grp[num] = 1


        return max(grp.values())

            

                



        
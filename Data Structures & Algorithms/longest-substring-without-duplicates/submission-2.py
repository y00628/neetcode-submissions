class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)

        if n <= 1:
            return n

        seen = {}
        longest = 0
        start, end = 0, 1

        while end <= n:
            seg = s[start:end]

            if len(set(seg)) < len(seg):
                longest = max(end-start-1, longest)
                start += 1
            
            end += 1


        return max(end-start-1, longest)


        # zxyzxyz
        # zxyxazy
        # z0 x3 y2
        # 3
        # bar raiser (raise to 1) c in seen and seen[c] > 1 (last idx)




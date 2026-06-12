from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_dist = Counter(s1)
        len_s1 = len(s1)

        for i in range(len(s2)-len_s1+1):
            if Counter(s2[i:i+len_s1]) == s1_dist:
                return True
        
        return False
        
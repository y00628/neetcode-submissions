from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_dist = Counter(s1)
        len_s1 = len(s1)
        s2_dist = Counter(s2[:len_s1])
        len_s2 = len(s2)

        if s2_dist == s1_dist:
            return True

        for i in range(1, len_s2-len_s1+1):
            s2_dist[s2[i-1]] -= 1
            s2_dist[s2[i+len_s1-1]] += 1

            if s2_dist == s1_dist:
                return True
            
        
        return False
        
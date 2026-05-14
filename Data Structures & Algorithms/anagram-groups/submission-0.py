from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for s in strs: # O(m)
            frq = [0] * 26 # O(1)

            for c in s: # O(n), n = length of longest word
                frq[ord(c) - ord("a")] += 1
            
            groups[tuple(frq)].append(s)

            


        return list(groups.values())

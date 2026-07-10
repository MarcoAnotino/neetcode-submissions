from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            tempL = [0] * 27 #[1,0,1,...,1,...,0]
            for c in s:
                tempL[ord(c) - ord("a")] += 1
            key = tuple(tempL)
            res[key].append(s)
        return list(res.values())

            

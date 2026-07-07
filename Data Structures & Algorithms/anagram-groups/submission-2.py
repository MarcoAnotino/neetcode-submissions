class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}

        for s in strs:
            tempList = [0] * 27
            for c in s:
                tempList[ord(c) - ord("a")] += 1
            
            key = tuple(tempList)

            if key not in res:
                res[key] = []
            
            res[key].append(s)
        return list(res.values())

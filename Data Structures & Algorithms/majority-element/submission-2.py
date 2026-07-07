from collections import defaultdict
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = defaultdict(int)
        for i in nums:
            count[i] += 1
        maxE = max(count.values())  
          
        for key, valor in count.items():
            if valor == maxE:
                return key

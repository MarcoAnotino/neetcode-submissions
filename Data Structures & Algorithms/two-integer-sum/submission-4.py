class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevValue = {}
        
        for i, num in enumerate(nums):
            diff = target - num
            if diff in prevValue:
                return [prevValue[diff], i] 
                 
            prevValue[num] = i
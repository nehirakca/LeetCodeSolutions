class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for ix1 in range(len(nums)):
            for ix2 in range(ix1+1,len(nums)):
                if target == nums[ix1]+nums[ix2]:
                    return [ix1,ix2]
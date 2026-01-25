class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i1 in range(len(nums)):
            for i2 in range(i1+1,len(nums)):
                if target == nums[i1]+nums[i2]:
                    return [i1,i2]
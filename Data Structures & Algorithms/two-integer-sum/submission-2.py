class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        checkedNums = {}
        for i, _ in enumerate(nums):
            diff = target - nums[i]
            if diff in checkedNums:
                return [checkedNums[diff], i]
            checkedNums[nums[i]] = i
        
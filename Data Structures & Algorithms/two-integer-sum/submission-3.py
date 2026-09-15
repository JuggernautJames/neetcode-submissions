class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        checkedNums = {}
        for i, value in enumerate(nums):
            diff = target - value
            if diff in checkedNums:
                return [checkedNums[diff], i]
            checkedNums[value] = i
        
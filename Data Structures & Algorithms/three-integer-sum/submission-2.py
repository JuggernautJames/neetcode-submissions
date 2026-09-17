from collections import Counter
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        for i, num in enumerate(nums):
            if num > 0:
                break;
            if i > 0 and num == nums[i-1]:
                continue;
            
            left = i+1
            right = len(nums) - 1
            while left < right:
                threeSum = nums[left] + nums[right] + num
                if (threeSum > 0):
                    right -= 1
                elif (threeSum < 0):
                    left += 1
                else:
                    ans.append([nums[left], nums[right], num])
                    left += 1
                    right -= 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
        return ans
        
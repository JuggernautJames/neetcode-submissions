class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        end = len(numbers) - 1
        while True:
            if i==end:
                break

            res = numbers[i] + numbers[end]
            if res == target:
                return [i+1, end+1]
            elif res < target:
                i+=1
            else:
                end-=1
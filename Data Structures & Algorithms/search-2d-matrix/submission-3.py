class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]: return False
        rows, cols = len(matrix), len(matrix[0])
        upper = rows*cols-1
        lower = 0
        while lower <= upper:
            curr = upper + lower // 2
            print(f"{lower}, {curr}, {upper}\n")
            arrValue = matrix[curr // cols][curr % cols]
            if arrValue == target: return True
            if arrValue < target:
                lower = curr + 1
            else:
                upper = curr - 1
        return False

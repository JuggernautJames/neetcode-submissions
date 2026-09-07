class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = {i: set() for i in range(9)}
        columns = {i: set() for i in range(9)}
        squares = {i: set() for i in range(9)}
        for row in range(9):
            for column in range(9):
                num = board[row][column]
                if num == ".":
                    continue
                square = (row // 3)*3 + (column//3)
                if (num in rows[row] or
                    num in columns[column] or
                    num in squares[square]):
                    return False
                rows[row].add(num)
                columns[column].add(num)
                squares[square].add(num)
        return True

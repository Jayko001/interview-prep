class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # check rows and columns
        for i in range(9):
            row = set()
            column = set()

            row_count = 0
            column_count = 0
            for j in range(9):
                if board[i][j] != ".":
                    row.add(board[i][j])
                    row_count += 1

                if board[j][i] != ".":
                    column.add(board[j][i])
                    column_count += 1

            if len(row) == row_count and len(column) == column_count:
                continue
            else:
                return False

        # check boxes
        for row_b in range(0,9,3):
            for row_c in range(0,9,3):

                box = set()
                box_count = 0
                for r in range(row_b, row_b+3):
                    for c in range(row_c, row_c+3):
                        if board[r][c] != ".":
                            box.add(board[r][c])
                            box_count += 1

                if len(box) == box_count:
                    continue
                else:
                    return False

        return True


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = {}
        columns = {}
        squares = {}

        for r in range(9):
            for c in range(9):
                val = board[r][c]

                if val == ".":
                    continue

                # initialize sets if not present
                if r not in rows:
                    rows[r] = set()
                if c not in columns:
                    columns[c] = set()
                box = (r // 3, c // 3)
                if box not in squares:
                    squares[box] = set()

                # duplicate check
                if (val in rows[r] or
                    val in columns[c] or
                    val in squares[box]):
                    return False

                # add value
                rows[r].add(val)
                columns[c].add(val)
                squares[box].add(val)

        print(squares)

        return True

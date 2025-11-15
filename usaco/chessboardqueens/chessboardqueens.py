from copy import deepcopy
import sys
from collections import defaultdict, Counter

FILENAME = "chessboardqueens"

# Renaming the read/write methods for convenience
input = sys.stdin.readline
write = sys.stdout.write


def print(*args, sep=" ", end="\n", file=sys.stderr):
    text = sep.join(str(arg) for arg in args)
    file.write(text)
    file.write(end)


def read():
    lines = []

    for _ in range(8):
        line = input().strip()
        lines.append(line)

    return lines


def solve():
    queens = read()
    queens = list(map(list, queens))

    place_queens(row=0, queens=queens, rem=8)
    return len(ans)


ans = []


def place_queens(row, queens, rem):
    if row >= len(queens) and rem <= 0:
        ans.append(queens)
        return

    if row >= len(queens):
        return

    cur_row = queens[row]

    # try to place queens on our current row
    for col_idx, pos in enumerate(cur_row):
        if pos == "*":
            continue

        if can_fit_col(col_idx, row, queens) and can_fit_diag(row, col_idx, queens):
            next_q = deepcopy(queens)
            next_q[row][col_idx] = "q"
            place_queens(row + 1, next_q, rem - 1)

    return


def can_fit_col(col, row, board):
    for row_idx in range(8):
        piece = board[row_idx][col]
        if piece == "q" and row != row_idx:
            return False

    return True


def can_fit_diag(
    row,
    col,
    board,
):
    dir = [(1, 1), (1, -1), (-1, -1), (-1, 1)]

    for mult in range(8):
        delta = [(x * mult + row, y * mult + col) for (x, y) in dir]
        for x, y in delta:
            if x > 7 or x < 0 or y > 7 or y < 0:
                continue

            if x == row and y == col:
                continue

            piece = board[x][y]
            if piece == "q":
                return False

    return True


solve()
write(str(len(ans)))


# for each row of the matrix,
# try to place a queen at every index in that row
# and iterate downwards
# def _solve():
#     for row in queens:
#         for idx, col in row:
#             place_queen(row, queens)
#     return

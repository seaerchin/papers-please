from typing import Tuple
import sys

FILENAME = "lostcow"

sys.stdin = open(f"{FILENAME}.in", "r")
sys.stdout = open(f"{FILENAME}.out", "w")

# Renaming the read/write methods for convenience
input = sys.stdin.readline
print = sys.stdout.write


def read_input() -> Tuple[int, int]:
    i = input()
    [x, y] = i.split(" ")

    return (int(x), int(y))


def solve():
    (x, y) = read_input()
    cur = x
    step = 1
    sign = 1
    travelled = 0
    y_greater = y > x

    if x == y:
        return 1

    while True:
        next_pos = x + step * sign
        step *= 2
        sign *= -1
        if y_greater and next_pos >= y:
            break
        if not y_greater and next_pos <= y:
            break
        travelled += abs(next_pos-cur)
        cur = next_pos

    travelled += abs(y - cur)
    return travelled


res = solve()

print(str(res))

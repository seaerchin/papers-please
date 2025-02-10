import sys

FILENAME = "pails"

sys.stdin = open(f"{FILENAME}.in", "r")
sys.stdout = open(f"{FILENAME}.out", "w")

# Renaming the read/write methods for convenience
input = sys.stdin.readline
write = sys.stdout.write


def read():
    [x, y, m] = input().split(" ")
    return [int(x), int(y), int(m)]


def _solve(x: int, y: int, m: int):
    if m % x == 0:
        return m

    # NOTE: now, we don't have clean divisor, so we take the largest
    times = m // x
    greatest = m - m % x

    for i in range(times+1):
        rem = m - i * x
        cur = i*x + (rem//y) * y
        greatest = max(cur, greatest)

    return greatest


def solve():
    [x, y, m] = read()
    x, y = _solve(x, y, m), _solve(y, x, m)
    write(str(max(x, y)))


solve()

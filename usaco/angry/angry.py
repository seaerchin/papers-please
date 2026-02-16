from itertools import takewhile
import sys
from collections import defaultdict, Counter

FILENAME = "angry"

sys.stdin = open(f"{FILENAME}.in", "r")
sys.stdout = open(f"{FILENAME}.out", "w")
sys.stderr = open(f"{FILENAME}.debug", "w")

# Renaming the read/write methods for convenience
input = sys.stdin.readline
write = sys.stdout.write


def print(*args, sep=" ", end="\n", file=sys.stderr):
    text = sep.join(str(arg) for arg in args)
    file.write(text)
    file.write(end)


def input_int():
    return list(map(lambda x: int(x), input().split(" ")))


def read():
    lines = int(input())
    res = []
    for _ in range(lines):
        res.append(int(input()))

    res.sort()
    return res


def solve():
    bales = read()
    res = -1
    for i in range(len(bales)):
        print("=== next ===")
        res = max(
            angry(
                bales[i],
                bales,
                1,
            ),
            res,
        )

    return res


def angry(
    cur_val,
    bales,
    radius,
):
    next_bigger = list(takewhile(lambda x: x <= cur_val + radius, bales))
    print("next_big", next_bigger)
    next_smaller = list(takewhile(lambda x: x >= cur_val - radius, reversed(bales)))
    print("next_sma", next_smaller)

    big_size = len(next_bigger)
    small_size = len(next_smaller)

    print("sizes", big_size, small_size)

    big = 0
    if big_size > 0:
        big = angry(max(next_bigger), bales[big_size:], radius + 1)

    small = 0
    if small_size > 0:
        small = angry(min(next_smaller), bales[:small_size], radius + 1)

    return 1 + big + small


res = solve()
write(f"{res}")

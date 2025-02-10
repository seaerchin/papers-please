from collections import defaultdict
import sys
from typing import Set

FILENAME = "gymnastics"

sys.stdin = open(f"{FILENAME}.in", "r")
sys.stdout = open(f"{FILENAME}.out", "w")

# Renaming the read/write methods for convenience
input = sys.stdin.readline
write = sys.stdout.write


def input_int():
    return list(map(lambda x: int(x), input().split(" ")))


def read():
    [lines, cows] = input().split(" ")
    perf = []
    for _ in range(int(lines)):
        perf.append(input_int())

    return perf


def generate(cows):
    pairs: list[tuple[int, int]] = []
    for idx, cow in enumerate(cows):
        prev = cows[:idx]
        for prev_cow in prev:
            pairs.append((prev_cow, cow))

    return pairs


def solve():
    perf = read()
    disallowed = defaultdict(bool)
    ans = set()
    for cows in perf:
        pairs = generate(cows)
        for pair in pairs:
            (x, y) = pair
            disallowed[pair] = True
            if disallowed[(y, x)]:
                if (y, x) in ans:
                    ans.remove((y, x))
                if pair in ans:
                    ans.remove(pair)
            else:
                ans.add(pair)

    write(str(len(ans)))


solve()

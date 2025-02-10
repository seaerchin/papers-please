import sys

FILENAME = "blist"

sys.stdin = open(f"{FILENAME}.in", "r")
sys.stdout = open(f"{FILENAME}.out", "w")

# Renaming the read/write methods for convenience
input = sys.stdin.readline
write = sys.stdout.write


def read():
    num_lines: int = int(input())
    ls: list[list[int]] = []
    for _ in range(num_lines):
        vars = list(map(lambda x: int(x), input().split(" ")))
        ls.append(vars)

    return ls


def solve():
    inputs = read()

    arr = [0] * 1000

    for [start, end, buckets] in inputs:
        for i in range(start, end):
            arr[i] += buckets

    ans = max(arr)
    write(str(ans))


solve()

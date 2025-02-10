import sys
from collections import defaultdict, Counter

FILENAME = "<FILE>"

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
    return


def solve():
    return


solve()

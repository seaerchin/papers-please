import sys
from collections import defaultdict, Counter

FILENAME = "lifeguards"

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
    [lines] = input_int()
    cows= []
    for _ in range(lines):
        [left, right] = input_int()
        cows.append((left,right))

    return cows 

def merge(cow, c):
    (left, right) = cow
    for i in range(left, right):
        c[i] = 1

    return c 


def cover(cow, covered):
    (left, right) = cow
    res = 0
    for i in range(left, right):
        if covered[i] == 0:
            res += 1

    return res

def solve():
    cows = read()
    largest = 0
    for (i, cow) in enumerate(cows):
        merged = [0 for i in range(1000)]
        rest = cows[:i] + cows[i+1:]
        for i in rest: 
            merged = merge(i, merged)
        largest = max(largest, sum(merged))


    return largest

res = solve()
write(str( res ))

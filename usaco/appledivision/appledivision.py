import sys
from collections import defaultdict, Counter

FILENAME = "appledivision"

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
    input()
    return input_int()


def generate_subsets(l):
    subsets = [[]]
    for elem in l:
        subsets += [curr + [elem] for curr in subsets]
    return subsets


def solve():
    n = read()
    subsets = generate_subsets(n)
    total = sum(n)
    min_diff = map(lambda x: calc_min_diff(total, x), subsets)
    return min(min_diff)


def calc_min_diff(total, subset):
    sum1 = sum(subset)
    sum2 = total - sum1
    return abs(sum1 - sum2)


output = solve()
print(output)
write(str(output))

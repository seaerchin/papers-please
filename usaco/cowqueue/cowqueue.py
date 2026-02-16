import sys
from collections import defaultdict, Counter

FILENAME = "cowqueue"

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


def output(*args, sep=" ", end="\n", file=sys.stdout):
    text = sep.join(str(arg) for arg in args)
    file.write(text)
    file.write(end)


def input_int():
    return list(map(lambda x: int(x), input().split(" ")))


def read():
    lines = input_int().pop()
    res = []
    for i in range(lines):
        res.append(input_int())
    return res


def solve():
    cows = read()
    cows.sort(key=lambda x: x[0])
    # ans will denote the current time interval
    ans = 0
    for [time, duration] in cows:
        # if the cow arrives after, we need to wait till that time
        ans = max(time, ans)
        # then we add the time it takes to process this cow
        ans += duration
    return ans


# we first read the input
# afterwards, sort by order of arrival
# then just count lol
write(str(solve()))

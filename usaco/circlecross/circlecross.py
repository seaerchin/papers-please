import sys
from collections import defaultdict, Counter

FILENAME = "circlecross"

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
    return input()


def solve():
    crossings = input()
    print(crossings)
    ans = 0
    seen = defaultdict(bool)
    # remember to handle 0, idx case
    for i, c in enumerate(crossings):
        (res, _seen) = scan(crossings, i, c, seen)
        ans += res
        seen = _seen

    write(str(ans))

# TODO: handle 0 case


def scan(crossings: str, i, c, seen):
    next_index = crossings.rfind(c)
    if next_index == -1:
        return 0
    inner_chars = crossings[i+1: next_index]
    res = 0
    for (char, count) in Counter(inner_chars).items():
        key = (c, char) if c > char else (char, c)
        if seen[key]:  # already seen
            continue
        if count == 1:
            seen[key] = True
            res += 1

    return (res, seen)


solve()

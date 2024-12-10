import sys
from typing import List, Tuple

FILENAME = "cowsignal"

sys.stdin = open(f"{FILENAME}.in", "r")
sys.stdout = open(f"{FILENAME}.out", "w")

# Renaming the read/write methods for convenience
input = sys.stdin.readline
print = sys.stdout.write


def read_input() -> Tuple[List[str], int, int]:
    i = input()
    [m, n, k] = i.split(" ")
    s: list[str] = []

    for _ in range(int(m)):
        s.append(input().strip())

    return (s, int(n), int(k))


def solve():
    (m, n, k) = read_input()
    res: list[str] = []
    for s in m:
        l = list(s)
        mm = "".join(list(map(lambda c: c * k, l)))
        for j in range(k):
            res.append(mm)

    return res


res = solve()

for i in res:
    print(i)
    print("\n")

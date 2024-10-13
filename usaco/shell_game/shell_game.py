import sys
from typing import List

sys.stdin = open("shell.in", "r")
sys.stdout = open("shell.out", "w")

# Renaming the read/write methods for convenience
input = sys.stdin.readline
print = sys.stdout.write

# sys.stdout.write requires you to format code manually
# print(str(num_lines) + "\n")

pos = [1, 2, 3]
points = [0, 0, 0]

num_lines = int(input().strip())


def split(s: str) -> List[int]:
    return list(map(int, s.split(" ")))


def solve() -> int:
    for i in range(num_lines):
        s = input()
        initial, to, guess = split(s)

        for (idx, p) in enumerate(pos):
            if initial == p or to == p:
                pos[idx] = initial if to == p else to
            if guess == pos[idx]:
                points[idx] += 1

    return max(points)


print(str(solve()))

from typing import List
import sys

FILENAME = "shuffle"

sys.stdin = open(f"{FILENAME}.in", "r")
sys.stdout = open(f"{FILENAME}.out", "w")

# Renaming the read/write methods for convenience
input = sys.stdin.readline
write = sys.stdout.write


def read():
    num_cows = int(input())
    shuffle = list(map(lambda x: int(x), input().split(" ")))
    cows = input().strip().split(" ")
    return (shuffle, cows)


def solve(shuffle: List[int], cows: List[str]):
    for i in range(3):
        cur = ["" for _ in range(len(cows))]
        for idx, to in enumerate(shuffle):
            cur[idx] = cows[to-1]

        cows = cur

    return cows


(shuffle, cows) = read()
res = solve(shuffle, cows)
for i in res:
    print(f"{i}")

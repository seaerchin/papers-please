
import sys
from typing import List, Tuple

FILENAME = "speeding"

sys.stdin = open(f"{FILENAME}.in", "r")
sys.stdout = open(f"{FILENAME}.out", "w")

# Renaming the read/write methods for convenience
input = sys.stdin.readline
print = sys.stdout.write


def read_input():
    road_segments, speed_segments = input().split(" ")
    road: List[int] = []
    driven: List[int] = []

    for _ in range(int(road_segments)):
        length, speed = input().split(" ")
        for _ in range(int(length)):
            road.append(int(speed))

    for _ in range(int(speed_segments)):
        length, speed = input().split(" ")
        for _ in range(int(length)):
            driven.append(int(speed))

    return zip(road, driven)


def solve():
    worst = 0
    zipped = read_input()
    m = map(lambda x: x[1] - x[0], zipped)
    # for (a, b) in zipped:
    #     worst = max(worst, b - a)
    # return worst
    return max(max(m), 0)


r = solve()
print(str(r))

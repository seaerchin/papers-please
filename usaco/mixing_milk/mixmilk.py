import sys
from typing import List, Tuple

FILENAME = "mixmilk"

sys.stdin = open(f"{FILENAME}.in", "r")
sys.stdout = open(f"{FILENAME}.out", "w")

# Renaming the read/write methods for convenience
input = sys.stdin.readline
print = sys.stdout.write


def read_input() -> List[List[int]]:
    res: List[List[int, ]] = []

    for _ in range(3):
        capacity, amount = input().strip().split(" ")
        t = [int(capacity), int(amount)]

        res.append(t)

    return res


OPS = [(0, 1), (1, 2), (2, 0)]


def solve() -> List[int]:
    # stores capacity, current amount
    buckets = read_input()
    for i in range(100):
        op_idx = i % 3
        a, b = OPS[op_idx]
        cur_amount_to = buckets[a][1]
        amount_pourable = buckets[b][0]-buckets[b][1]

        if amount_pourable >= cur_amount_to:
            buckets[a][1] = 0
            buckets[b][1] += cur_amount_to

        # overflow
        else:
            buckets[a][1] -= amount_pourable
            buckets[b][1] = buckets[b][0]

    return list(map(lambda x: x[1], buckets))


res = solve()

for i in res:
    print(str(i))
    print("\n")

import sys
from collections import defaultdict, Counter

FILENAME = "cowllege"

# Renaming the read/write methods for convenience
input = sys.stdin.readline
write = sys.stdout.write


def input_int():
    return list(map(lambda x: int(x), input().split(" ")))


def read():
    n = int(input())
    costs = input_int()
    costs.sort()
    assert len(costs) == n

    return costs


def solve():
    # scan through the array in order
    # then for each item, record down num items before
    costs = read()
    l = len(costs)
    res = 0
    ans_cost = 0
    for i, cost in enumerate(costs):
        cur_cost = (l - i) * cost
        new_res = max(res, cur_cost)
        if new_res > res:
            res = new_res
            ans_cost = cost

    return [res, ans_cost]


[a, b] = solve()
print(a, b)

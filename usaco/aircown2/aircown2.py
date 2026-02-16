import sys
import math
from collections import defaultdict, Counter

# Renaming the read/write methods for convenience
input = sys.stdin.readline
write = sys.stdout.write


# [1, 2, 3, 4, 5, 6]
# cow1 = [2, 4] -> cooled by: 3
# [1, 2, 3]
# 1: [1, 2, 3] (3 units)


def print(*args, sep=" ", end="\n", file=sys.stderr):
    text = sep.join(str(arg) for arg in args)
    file.write(text)
    file.write(end)


def input_int():
    return list(map(lambda x: int(x), input().strip().split(" ")))


def read():
    [n_cows, n_aircons] = input_int()
    cows = []
    ac = []
    for _ in range(n_cows):
        cows.append(input_int())

    for _ in range(n_aircons):
        ac.append(input_int())

    print(cows)

    return [cows, ac]


ac = []


def solve():
    cows, _ac = read()
    stalls = [0 for i in range(101)]
    global ac
    for [start, end, v] in cows:
        for i in range(start, end + 1):
            stalls[i] += v

    ac = _ac
    try_stall([], stalls, 0)

    # arr = cows
    # for i in aircons:
    #   if any_cow in aircon_range > 0:
    #       cows_in_aircon_range -= aircon_power
    #       cost += aircon_cost
    #       recurse_down(rem_aircon, cows)
    #
    return


def update_cows(ac, cows):
    [start, end, cooling, _] = ac
    new_cows = cows[:]
    for i in range(start, end + 1):
        new_cows[i] -= cooling

    return new_cows


cost = 9 * 110000000000000000000000000000000000000000


# ac chosen, state of stall, current index in global ac set
def try_stall(cur_acs, stalls, cur):
    if all(list(map(lambda x: x <= 0, stalls))):
        global cost
        ac_cost = sum(map(lambda x: x[3], cur_acs))
        cost = min(ac_cost, cost)
        return

    global ac

    if cur == len(ac):
        return

    cur_ac = ac[cur]
    cur_acs.append(cur_ac)
    new_stalls = update_cows(cur_ac, stalls)
    try_stall(cur_acs, new_stalls, cur + 1)
    cur_acs.pop()
    try_stall(cur_acs, stalls, cur + 1)


solve()
write(str(cost))

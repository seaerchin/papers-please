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
    ac=[]
    for _ in range(n_cows): 
        cows.append(input_int())

    for _ in range(n_aircons): 
        ac.append(input_int())

    print(cows)

    return [cows, ac]



def solve():
    cows, ac = read()
    stalls= [0 for i in range(101)]
    for [start, end, v] in (cows):
        for i in range(start, end+1):
            stalls[i] += v

    try_stall(ac, stalls, 0)



    # arr = cows
    # for i in aircons:
    #   if any_cow in aircon_range > 0:
    #       cows_in_aircon_range -= aircon_power
    #       cost += aircon_cost
    #       recurse_down(rem_aircon, cows)
    #
    return


def update_cows(stall, cows):
    [start, end, cooling, _] = stall
    new_cows = cows[:]
    for i in range(start, end+1):
        new_cows[i] -= cooling

    return new_cows


cost = 9*110000000000000000000000000000000000000000

def try_stall(ac, stalls, cur):
    if all(list(map(lambda x: x<=0, stalls))): 
        global cost
        cost = min(cur, cost)

    for idx, stall in enumerate(ac):
        next_stalls=ac[:idx]+ac[idx+1:]
        # update cows here
        updated_cows = update_cows(stall,stalls)
        try_stall(next_stalls, updated_cows, cur+stall[3])
    

solve()
write(str(cost))


import sys
from collections import defaultdict, Counter

FILENAME = "cownomics"

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
    [cows, chars] = input_int()
    spotty = []
    plain = []
    for i in range(2):
        for cow in range(cows):
            if i % 2 == 0:
                spotty.append(input().strip())
            else:
                plain.append(input())

    return ((spotty, plain), chars)


def solve():
    ((spotty, plain), chars) = read()
    # now each is a list of len M
    all_spots = zip(*spotty)
    all_plain = zip(*plain)
    all = zip(all_spots, all_plain)
    # we will store [spotted_genes, plain_genes]
    genes = []
    for i, (spot, plain) in enumerate(all):
        # check if any overlap
        spot_set = set(spot)
        plain_set = set(plain)
        print(i, spot, plain)
        if (spot_set.isdisjoint(plain_set)):
            genes.append(i)

    write(str(len(genes)))


solve()

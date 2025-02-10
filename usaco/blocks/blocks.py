from collections import defaultdict, Counter
import sys

FILENAME = "blocks"

sys.stdin = open(f"{FILENAME}.in", "r")
sys.stdout = open(f"{FILENAME}.out", "w")

# Renaming the read/write methods for convenience
input = sys.stdin.readline
write = sys.stdout.write


class Reader():

    letters = defaultdict(int)

    def __init__(self):
        self.letters = defaultdict(int)

    def read(self, s: str, ss: str):
        for c in s:
            self.letters[c] += 1

        letter_count = Counter(s)
        sec_count = Counter(ss)
        for [let, count] in sec_count.items():
            if letter_count[let] < count:
                self.letters[let] += count - letter_count[let]


def read():
    num_lines = int(input())
    r = Reader()
    for _ in range(num_lines):
        [first, second] = input().split(" ")
        r.read(first, second)
    return r


def solve():
    r = read()
    for i in range(97, 97 + 26):
        c = chr(i)
        print(r.letters[c])


solve()

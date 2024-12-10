from typing import Tuple
import sys

FILENAME = "<FILE>"

sys.stdin = open(f"{FILENAME}.in", "r")
sys.stdout = open(f"{FILENAME}.out", "w")

# Renaming the read/write methods for convenience
input = sys.stdin.readline
write = sys.stdout.write

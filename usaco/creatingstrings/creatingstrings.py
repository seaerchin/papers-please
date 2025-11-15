import sys

FILENAME = "creatingstrings"

# Renaming the read/write methods for convenience
input = sys.stdin.readline
write = sys.stdout.write


def print(*args, sep=" ", end="\n", file=sys.stderr):
    text = sep.join(str(arg) for arg in args)
    file.write(text)
    file.write(end)


ans = set()


# cur is a string consisting of what we have so far
def generate(
    cur,
    remaining,
):
    if len(remaining) == 0:
        ans.add(cur)
        return

    for i in range(len(remaining)):
        next = remaining[i]
        next_cur = cur + next
        next_remaining = remaining[0:i] + remaining[i + 1 :]
        generate(next_cur, next_remaining)


def read():
    return


def solve():
    s = "".join(sorted(input().strip()))
    return generate("", s)


solve()
write(str(len(ans)))
write("\n")
for i in sorted(list(ans)):
    write(str(i))
    write("\n")

# n glasses, each with cap of 1..N
# we want to pour exactly K liters

# probably greedy -> if we can use a bigger glass, we should always use
# impossible if the sum of glasses < water


# n is glasses, k is water
def glasses(n: int, k: int) -> int:
    if sum([i for i in range(n)]) > k:
        return -1

    # already hit
    if k == 0:
        return 1

    # take the largest n that fits k
    if k <= n:
        return 1

    return glasses(k - n, k) + 1

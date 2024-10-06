from collections import Counter

# maintain a heap of the smallest items, together with those that have not been processed
# at every iteration, shift an element over and update accordingly


class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        res = set[list[int]]()

        # smallest will be the current item
        # counter will hold the list of item

        def solve(counter: Counter[int], cur: list[int], target: int) -> None:
            if target == 0:
                res.add(cur)

            acceptable = filter(lambda x: x <= target, set(counter))

            for i in acceptable:
                inner = counter
                inner[i] -= 1
                solve(inner, cur + [i], target - i)

        return list(res)

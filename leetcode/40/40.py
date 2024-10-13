class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        res: list[list[int]] = []

        candidates.sort()
        # candidates has to be sorted prior to going in

        def solve(candidates: list[int], target: int, cur: list[int]):
            if target == 0:
                res.append(cur)
            if target < 0:
                return

            for idx, num in enumerate(candidates):
                solve(candidates[idx + 1:], target - num, cur + [num])

            return

        solve(candidates, target, [])

        return res

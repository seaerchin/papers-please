class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        res: list[list[int]] = []
        nums.sort()
        l = len(nums)

        # another backtracking problem
        def solve(cur: list[int], idx: int):
            res.append(cur)

            if len(nums) == idx:
                return

            for i in range(idx, l):
                num = nums[i]
                if i > idx and nums[i] == nums[i - 1]:
                    continue
                solve(cur + [num], i+1)

            return

        solve([], 0)

        return res

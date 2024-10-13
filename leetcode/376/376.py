class Solution:
    def wiggleMaxLength(self, nums: list[int]) -> int:
        l = len(nums)

        def solve(curIdx: int, prevDiff: int, longest: int) -> int:
            if curIdx == len(nums):
                return longest

            curLongest = longest
            for i in range(curIdx, l):
                # do bounds checking here
                if curIdx == 0:
                    longest_at_index = max(
                        solve(1, nums[1], 1),  solve(1, 0-nums[1], 1))
                    curLongest = max(longest, longest_at_index)

                prev = nums[curIdx - 1]
                diff = prev - nums[i]

                if diff == 0:
                    continue
                if prevDiff > 0 and diff > 0:
                    continue
                if prevDiff < 0 and diff < 0:
                    continue

                longest_at_index = solve(i + 1, diff, longest + 1)
                curLongest = max(longest, longest_at_index)

            return curLongest

            # must remember to not accept any number that is equal to my current number

        return solve(0,  0, 0)


from typing import List, Tuple


class Solution:
    def rob(self, nums: List[int]) -> int:

        def solve(took_prev: List[int], skipped_prev: List[int], cur_pos: int, rest: List[int]) -> Tuple[List[int], List[int]]:
            if len(rest) == 0:
                return (took_prev, skipped_prev)

            # find the current max that you have at your position
            best_if_take_prev = 0 if len(took_prev) == 0  else max(took_prev[:cur_pos])
            best_if_skipped = 0 if len(skipped_prev) == 0 else  max(skipped_prev[:cur_pos]) + nums[cur_pos] 

            took_prev.append(max(best_if_skipped, best_if_take_prev))
            skipped_prev.append(max(best_if_take_prev,(0 if len(skipped_prev) == 0 else max(skipped_prev[:cur_pos]))))
            return solve(took_prev, skipped_prev, cur_pos + 1, rest[1:])

        
        (took, skipped) = solve([], [], 0, nums)

        return max(took[-1], skipped[-1])

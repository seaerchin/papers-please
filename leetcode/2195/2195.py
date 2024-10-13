import heapq


class Solution:
    def minimalKSum(self, nums: list[int], k: int) -> int:
        # smallest that i can get from here
        # [1, k]
        s = k/2 * (2 + (k-1))
        ptr = k + 1
        heapq.heapify(nums)
        while (len(nums) > 0 and nums[0] <= k):
            cm = heapq.heappop(nums)
            s -= cm
            s += ptr
            ptr += 1
        return int(s)

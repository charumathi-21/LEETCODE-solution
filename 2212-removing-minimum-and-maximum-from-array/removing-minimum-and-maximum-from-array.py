class Solution:
    def minimumDeletions(self, nums):
        n = len(nums)

        min_pos = nums.index(min(nums))
        max_pos = nums.index(max(nums))

        left = min(min_pos, max_pos)
        right = max(min_pos, max_pos)

        # Option 1: Remove both from the front
        front = right + 1

        # Option 2: Remove both from the back
        back = n - left

        # Option 3: Remove min/max from opposite ends
        opposite = (left + 1) + (n - right)

        return min(front, back, opposite)
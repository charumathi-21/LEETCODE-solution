class Fenwick(object):
    def __init__(self, n):
        self.bit = [0] * (n + 2)

    def update(self, i, val):
        while i < len(self.bit):
            self.bit[i] += val
            i += i & -i

    def query(self, i):
        s = 0
        while i > 0:
            s += self.bit[i]
            i -= i & -i
        return s


class Solution(object):
    def countMajoritySubarrays(self, nums, target):
        n = len(nums)

        prefix = [0]
        s = 0
        for x in nums:
            if x == target:
                s += 1
            else:
                s -= 1
            prefix.append(s)

        vals = sorted(set(prefix))
        rank = {}
        for i, v in enumerate(vals):
            rank[v] = i + 1

        bit = Fenwick(len(vals))
        ans = 0

        for p in prefix:
            idx = rank[p]
            ans += bit.query(idx - 1)
            bit.update(idx, 1)

        return ans
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        feq = {}

        for i in nums:
            if i not in feq:
                feq[i] = 1
            else:
                feq[i] += 1

        values = sorted(feq.values())
        frequent = []

        while len(frequent) < k:
            target_freq = values.pop()
            for key, val in list(feq.items()):
                if val == target_freq:
                    frequent.append(key)
                    del feq[key]
                    break

        return frequent
                




        
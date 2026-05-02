class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        triplets = set()

        numlen = len(nums)
        for i in range(numlen):
            j = i + 1
            k = numlen - 1

            while j < k:
                tot = nums[i] + nums[j] + nums[k]
                if tot == 0:
                    triplets.add((nums[i], nums[j], nums[k]))
                    k -= 1
                    j += 1
                elif tot > 0:
                    k -= 1
                else:
                    j += 1
        
        return list(triplets)
class Solution:

    def removeDuplicates(self, nums: list[int]) -> int:
        lastIndex = 1
        for i in range(len(nums)-1):
            if nums[i] != nums[i + 1]:
                nums[lastIndex] = nums[i + 1]
                lastIndex += 1
        return lastIndex, nums


solution = Solution()
result = solution.removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4])
print(result)

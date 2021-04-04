from time import sleep

# Tentado enteder porque leva tempo para processar essa criptografia
class Solution:
    def twoSum(self, nums, target):

        for i in range(0, len(nums)):
            sleep(1)
            print(f"{i=}")

            for j in range(i + 1, len(nums)):

                print(f"{j=}")

                if nums[i] + nums[j] == target:

                    return [i, j]

        return None


nums = [11, 15, 2, 7]
target = 9

exibi = Solution().twoSum(nums, target)

print(exibi)
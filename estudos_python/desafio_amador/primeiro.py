from time import sleep


# Tentado enteder porque leva tempo para processar essa criptografia
class Solution:
    def twoSum(self, nums, target):

        for i in range(0, len(nums)):
            sleep(1)
            print(f"{i=}")

            for k in range(i + 1, len(nums)):

                print(f"{k=}")

                if nums[i] + nums[k] == target:

                    return [i, k]

        return None


nums = [11, 15, 2, 7]
target = 9

exibi = Solution().twoSum(nums, target)

print(exibi)

# https://leetcode.com/problems/two-sum/
# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# Brute force: Check each set of numbers. Can toss out numbers bigger than sum

# Need to work backwards from the target number.
# Start at the target number, is t - 1 and 1 an option?
# If the nums list is sorted this could be solid. If t = 10 we only need to check 1-5 and for counters
# 1 2 3 4 5 6 7

# This works, but it's not optimal
class Solution:
    def twoSum(self, nums, target):
        # create a list of numbers up to half of the target
        checkList = range(target // 2)

        for checkItem in checkList:
            inverse = target - checkItem
            if checkItem in nums and inverse in nums:
                return (nums.index(checkItem), nums.index(inverse))

        return (-1, -1)


# Can I make a more optimal solution?

# Splat all possible combinations into a look up list? Seems slow

# Implement the one pass hash solution
class Solution2:
    def twoSum(self, nums, target):
        valuesDict = {}

        for index, value in enumerate(nums):
            valuesDict[value] = index

        return (-1, -1)


# Test solution
lista = [1, 2, 3, 4, 5]
listb = [23, 45, 123, 4, 17, 81]

mySolution = Solution()
solution = mySolution.twoSum(lista, 6)
print(str(solution))
solution = mySolution.twoSum(listb, 49)
print(str(solution))

mySolution2 = Solution2()
solution = mySolution2.twoSum(listb, 49)

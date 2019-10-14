# Given a list of numbers and a number sum, return whether
# any two numbers from the list add up to sum.
# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

# time comlexity of the below soulution - O(n)
# Space complexity of the below soulution - O(n)

nums = [10, 15, 3, 7]
sum = 19


def add_nums_to_get_sum(nums, sum):
    # create a hash set
    s = set()

    for i in range(len(nums)):
        temp = sum - nums[i]
        if temp in s:
            return True
        s.add(nums[i])

    return False


print(add_nums_to_get_sum(nums, sum))


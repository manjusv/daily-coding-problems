nums = [2, 11, 6, 2, 5]


def find_max_sum(nums):
    # incl is the max sum including the current element
    incl = nums[0]
    # excl is the max sum excluding the current element
    excl = 0
    n = len(nums)

    # keep updating the incl and excl looping through all elements from index 1
    for i in range(1, n):
        new_excl = max(incl, excl)

        incl = excl + nums[i]
        excl = new_excl

    return max(incl, excl)


print(find_max_sum(nums))

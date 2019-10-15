# find the smallest positive number missing from an unsorted array
nums = [-1, 3, 6, 4, 2, 5, 7]


def missing_positive_number(nums):
    # if the list contains a single element
    if len(nums) == 1:
        return 1 if nums[0] < 1 else 2

    max_value = max(nums)

    if max_value < 1:
        # if all the values in list are -ve numbers
        return 1

    # create a list of 0's of size max_value
    temp = [0] * max_value

    # for all positive integers, change the index value in temp to 1
    for i in range(len(nums)):
        if nums[i] > 0:
            if temp[nums[i] - 1] != 1:
                temp[nums[i] - 1] = 1

    # check for first 0 in temp list and return its index + 1
    for i in range(len(temp)):
        if temp[i] == 0:
            return i + 1

    return i + 2


print(missing_positive_number(nums))

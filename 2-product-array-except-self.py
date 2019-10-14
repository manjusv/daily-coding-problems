# Given an array of integers, return a new array such that each element
# at index i of the new array is the product of all the numbers in
# the original array except the one at i.
# Time complexity of below solution - O(n)

nums = [1, 2, 3, 4, 5]

# initialize product list to all 1's
n = len(nums)
product = [1] * n
temp = 1

# in below loop, temp variable contains product of all elements on
# left side, excluding element at index i
for i in range(n):
    product[i] = temp
    temp *= nums[i]

# Initialize temp to 1 for product on right side
temp = 1

# in below loop, temp variable contains product of all elements on
# right side, excluding element at index i
for i in range(n - 1, -1, -1):
    product[i] *= temp
    temp *= nums[i]

# print the new array
print(product)

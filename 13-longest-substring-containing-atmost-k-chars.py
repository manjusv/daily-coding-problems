# Given an integer k and a string s, find the length of the longest
# substring that contains at most k distinct characters.
# For example, given s = "abcba" and k = 2, the longest
# substring with k distinct characters is "bcb".

# time complexity of the solution is O(n * k) where n is length of s
# space complexity is O(k)


def length_of_longest_substring_k_distinct_chars(s, k):
    # base case
    if k == 0:
        return 0

    lower_bound = 0
    upper_bound = 0

    # dict stores the last index of last occurance of a char in the string
    dict = {}
    max_length = 0

    for i, char in enumerate(s):
        dict[char] = i

        if len(dict) <= k:
            new_lower_bound = lower_bound
        else:
            # pop the last occuring char from dict
            key_to_pop = min(dict)
            new_lower_bound = dict.pop(key_to_pop) + 1

        lower_bound = new_lower_bound
        upper_bound = upper_bound + 1
        max_length = max(max_length, upper_bound - lower_bound)

    return max_length


s = "aabacbebebe"
k = 3
print(length_of_longest_substring_k_distinct_chars(s, k))

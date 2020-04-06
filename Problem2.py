from functools import reduce

# Given an array of integers, return a new array such that
# each element at index i of the new array is the product of all
# the numbers in the original array except the one at i.

# For example, if our input was [1, 2, 3, 4, 5],
# the expected output would be [120, 60, 40, 30, 24].
# If our input was [3, 2, 1], the expected output would be [2, 3, 6].

# Follow-up: what if you can't use division?


def products(nums):
    total = reduce(lambda x, y: x*y, nums)
    newlist = list()
    for elem in nums:
        newlist.append(total/elem)
    return newlist


def products_no_division(nums):

    # Generates prefixes, product of numbers to element i
    prefixes = list()
    for elem in nums:
        if prefixes:
            prefixes.append(elem * prefixes[-1])
        else:
            prefixes.append(elem)

    # Generate prefixes, product of numbers from i to end.
    suffixes = list()
    for elem in reversed(nums):
        if suffixes:
            suffixes.insert(0, elem * suffixes[0])
        else:
            suffixes.append(elem)
    print(prefixes, suffixes)

    results = list()
    for i, _ in enumerate(nums):
        if i == 0:
            results.append(suffixes[i+1])
        elif i == len(nums) - 1:
            results.append(prefixes[i-1])
        else:
            results.append(prefixes[i-1] * suffixes[i+1])
    return results

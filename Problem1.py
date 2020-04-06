from itertools import combinations


# Given a list of numbers and a number k,
# return whether any two numbers from the list add up to k.

# For example, given [10, 15, 3, 7] and k of 17,
# return true since 10 + 7 is 17.

# Bonus: Can you do this in one pass?


# Checks for 2sum by iterating through all combinations of the list
# of numbers. Worst case takes O(n choose 2) = (n^2 - n)/2 = O(n^2)
def twosum_naive(nums, k):
    for elem in combinations(nums, 2):
        print(elem)
        if sum(elem) == k:
            return True
    return False


# Checks for 2sum only iterating through the list once. Every step it checks
# if the current number can be used to sum to k, if not it adds k - elem to
# vals, the number that would needed to be added to elem to get to k. Since
# checking for membership of a set is O(1), this algorithm is O(n)
def twosum(nums, k):
    vals = set()
    for elem in nums:
        if elem in vals:
            return True
        else:
            vals.add(k - elem)
    return False

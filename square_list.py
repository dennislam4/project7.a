# Author: Dennis Lam
# GitHub username: dennislam4
# Date: 7/13/2022
# Description: A function that takes as a list of numbers and replaces each value with the
# square of that value.

def square_list(nums):
    """Mutates and returns list of numbers into a list of their squared versions."""
    for i in range(len(nums)):
        nums[i] = (nums[i] ** 2)

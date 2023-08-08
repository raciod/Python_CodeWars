# #_Problem_ :
"""
Sum of positive

You get an array of numbers, return the sum of all of the positives ones.

Example [1,-4,7,12] => 1 + 7 + 12 = 20

Note: if there is nothing to sum, the sum is default to 0.
"""
# #_solution :

def positive_sum(arr):
    positive_nums = [num for num in arr if num > 0]
    return sum(positive_nums)

# Test
arr = [-1, -4, -7, -12]
print(positive_sum(arr))  # Output: 0

#######################################################
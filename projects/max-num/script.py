'''
Create a function named max_num() that takes a list of numbers named nums as a parameter.

The function should return the largest number in nums

Note: don't use the built-in max() function
'''

def max_num(nums):
  maximum = nums[0]
  for num in nums:
    if num > maximum:
      maximum = num
  return maximum

# Tests the function
print(max_num([50, -10, 0, 75, 20]))
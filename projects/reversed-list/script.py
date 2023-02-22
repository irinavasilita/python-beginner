'''
Create a function named reversed_list() that takes two lists of the same size as parameters named lst1 and lst2.

The function should return True if lst1 is the same as lst2 reversed. The function should return False otherwise.

For example, reversed_list([1, 2, 3], [3, 2, 1]) should return True.

We are going to test two lists to see if the second list is the reverse of the first list. 
There are a few different ways to approach this, but we are going to try a method that iterates through each 
of the values in one direction for the first list and compares them against the values starting from the other 
direction in the second list.
'''

def reversed_list(lst1, lst2):
  for i in range(len(lst1)):
    if lst1[i] != lst2[-(i+1)]:
    # or if lst1[i] != lst2[len(lst2) - 1 - i]:
      return False
  return True

# Tests the function
print(reversed_list([1, 2, 3], [3, 2, 1]))
print(reversed_list([1, 5, 3], [3, 2, 1]))
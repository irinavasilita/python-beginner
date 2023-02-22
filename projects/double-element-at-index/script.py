'''
Create a function named double_index that has two parameters: a list named my_list and a single number named index.

The function should return a new list where all elements are the same as in my_list except for the element at index. 
The element at index should be double the value of the element at index of the original my_list.

If index is not a valid index, the function should return the original list.

For example, the following code should return [1,2,6,4] because the element at index 2 has been doubled:

double_index([1, 2, 3, 4], 2)

Note: the index is always a positive number or 0.
'''
def double_index(my_list, index):
  # Checks if index is out of range
  if index >= len(my_list):
    return my_list
  
  # Gets the original list up to index
  new_list = my_list[:index]
  # Adds double the value at index to the new list
  new_list.append(my_list[index]*2)
  # Adds the rest of the original list
  new_list = new_list + my_list[index+1:]
  return new_list


# Testing
print(double_index([3, 8, -10, 12], 2))


'''
Note that this solution is careful not to modify the original input list. 
If we were to simply use my_list[index] = my_list[index] * 2 then the list 
that was passed into the function would be modified outside of the function as well. 
Creating a new list and writing the values to it prevents this from happening. 
We use slicing to extract the values before and after the index and we append 
the modified value at the index to our new list.
'''
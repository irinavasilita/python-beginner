'''
Create a function called middle_element that has one parameter named my_list.

If there are an odd number of elements in my_list, the function should return 
the middle element. If there are an even number of elements, the function should 
return the average of the middle two elements.
'''

def middle_element(my_list):
  length = len(my_list)
  half_len = int(length/2)

  if length%2 == 0:
    middle = (my_list[half_len-1] + my_list[half_len]) / 2
  else:
    middle = my_list[half_len]
    
  return middle

# Testing
print(middle_element([5, 2, -10, -4, 4, 5]))
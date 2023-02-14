'''
Exercise to practice Python lists.

Imagine there is a new pastry shop in your city 
and you are helping them organize some data.
'''
# To keep track of the kinds of pastries you sell, 
# create a list called pastries
pastries = ['croissant', 'bizcocho', 'cherry pie', 'pecan pie', 'empanada', 'mille-feuille', 'cannoli']

# To keep track of how much each kind of pastry costs, 
# create a list called prices 
prices = [12.99, 16.99, 8.99, 2.99, 8.99, 14.99, 18.99]

# Find the number of pastries that cost 8.99 dolars
num_eight_dollars_pastries = prices.count(8.99)
print(num_eight_dollars_pastries)

# Find the number of pastries in the menu
num_pastries = len(pastries)
print('We sell', num_pastries,'different kind of pastries!')

'''Use the existing data about the pizza toppings 
and prices to create a new two-dimensional list called 
pastries_and_prices. For this new list make sure the 
prices come before the pastry name.

Note: You don’t need to use your original pastries 
and prices lists in this exercise. Create a new 
two-dimensional list from scratch.
'''
pastries_and_prices = [
  [12.99,'croissant'],
  [16.99, 'bizcocho'],
  [8.99, 'cherry pie'],
  [2.99, 'pecan pie'],
  [8.99, 'empanada'],
  [14.99, 'mille-feuille'],
  [18.99, 'cannoli']
]

print(pastries_and_prices)

# Sort the pastries_and_prices so that the 
# pastries are in the order of increasing price (ascending).
pastries_and_prices.sort()
print(pastries_and_prices)

# Get the cheapest pastry for one client
cheapest_pastry = pastries_and_prices[0]
print(cheapest_pastry)

# Get the priciest pastry for one client
priciest_pizza = pastries_and_prices[-1]

# The last client bought the last item of the priciest pastry.
# Remove it from the list
pastries_and_prices.pop()
print(pastries_and_prices)

# Since there is no more cannoli, you want to add a new pastry 
# called "pionono" to keep the customers excited about new pastries.
# Note: Make sure to position it relative to the rest of the sorted data 
# in pastries_and_prices, otherwise our data will not be correctly sorted anymore! 
pastries_and_prices.insert(1, [5.99, 'pionono'])
print(pastries_and_prices)

# A client requested the first three cheapest pastries
# Create a new list of them.
three_cheapest = pastries_and_prices[:3]
print(three_cheapest)
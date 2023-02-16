'''
Exercise to practice loops and lists comprehensions.

Imagine you help a hair salon and you must analyze some data.
'''

# You are provided with three lists: 
# hairstyles: the names of the cuts offered
# prices: the price of each hairstyle in the hairstyles list
# last_week: the number of purchases for each hairstyle type in the last week
hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]
prices = [30, 25, 40, 20, 20, 35, 50, 35]
last_week = [2, 3, 5, 8, 4, 4, 6, 2]

# 1. Find out the average price of the cut.
total_price = 0

for price in prices:
  total_price=+price

average_price = total_price/len(prices)
print(f'Average Haircut Price: {average_price}')

# 2. The salon owner want to cut the price by 5 dollars.
# Use a list comprehension to make a list called new_prices, which has each element in prices minus 5.
new_prices = [price-5 for price in prices]
print(new_prices)

# 3. Find how much revenue was brought in last week.
total_revenue = 0

for i in range(len(hairstyles)):
  total_revenue += prices[i] * last_week[i]

print(f'Total Revenue: {total_revenue}')

# 4. Find the average daily revenue.
average_daily_revenue = total_revenue/7
print(average_daily_revenue)

# 5. Create a new list called cuts_under_30, 
# that contains all the cuts for which the new price is less than 30.
cuts_under_30 = [hairstyles[i] for i in range(len(new_prices)) if new_prices[i]<30]
print(cuts_under_30)
'''
Create a function called win_percentage() that takes two parameters named wins and losses.

This function should return out the total percentage of games won by a team based on these two numbers.
'''

def win_percentage(wins, losses):
  total_games = wins + losses
  ratio = wins / total_games
  return ratio * 100

# Tests the funciton
# should print 50
print(win_percentage(5, 5))
# should print 100
print(win_percentage(10, 0))
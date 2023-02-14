'''
Exercise to practice the if/else statements.

Read the README.md file.
'''

import random

name = input('What is your name?\n')
question = input('Enter the question you want to ask the Magic 8-ball.\n')

# Generates a random number between 1 (inclusive) and 9 (inclusive)
random_no = random.randint(1,9)
answer = ''

if random_no == 1:
  answer = 'Yes - definitely.'
elif random_no == 2:
  answer = 'It is decidedly so.'
elif random_no == 3:
  answer = 'Without a doubt.'
elif random_no == 4:
  answer = 'Reply hazy, try again.'
elif random_no == 5:
  answer = 'Ask again later.'
elif random_no == 6:
  answer = 'Better not tell you now.'
elif random_no == 7:
  answer = 'My sources say no.'
elif random_no == 8:
  answer = 'Outlook not so good.'
elif random_no == 9:
  answer = 'Very doubtful.'
else:
  answer = 'Error'

if name and question:
    print(f'{name} asks: {question}')
    print(f'Magic 8-Ball answer: {answer}')
elif question:
    print(f'Question: {question}')
    print(f'Magic 8-Ball answer: {answer}')
else:
    print('Input error.')

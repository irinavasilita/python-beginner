'''
Exercise to practice dictionaries in Python.

Find the user's weight on other planets.
'''

import pprint

# Relative Gravity of the Planets (Source: NASA)
relative_gravity = {
    "Moon": 0.166,
    "Jupiter": 2.36,
    "Saturn": 0.916,
    "Neptune": 1.12,
    "Uranus": 0.889,
    "Venus": 0.907,
    "Mars": 0.377,
    "Mercury": 0.378,
    "Pluto": 0.071
}

user_input = float(input('How much do you weight on Earth?\n'))
user_weights = {key: value * user_input for key, value in relative_gravity.items()}
pprint.pprint(user_weights)
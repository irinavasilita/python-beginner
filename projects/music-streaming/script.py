'''
Exercise to practice disctionaries
'''
songs = ['Like a Rolling Stone', 'Satisfaction', 'Imagine', 'What\'s Going On', 'Respect', 'Good Vibrations']
playcounts = [78, 29, 44, 21, 89, 5]

'''
Using a dict comprehension, create a dictionary called plays that goes 
through zip(songs, playcounts) and creates a song:playcount pair for 
each song in songs and each playcount in playcounts.
'''
plays = {song: playcount for song, playcount in zip(songs, playcounts)}
print(plays)

'''
Add a new entry to it. The entry should be for the song "Purple Haze" 
and the playcount is 1.
'''
plays['Purple Haze'] = 1

'''
This user has caught Aretha Franklin fever and listened to “Respect” 
5 more times. Update the value for "Respect" to be 94 in the plays dictionary.
'''
plays['Respect'] = 94

'''
Create a dictionary called library that has two key: value pairs:

- key "The Best Songs" with a value of plays, the dictionary you created
- key "Sunday Feelings" with a value of an empty dictionary
'''

library = {'The Best Songs': plays, 'Sunday Feelings': {}}
print(library)
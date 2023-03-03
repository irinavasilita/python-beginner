'''
You have been delivered a string that contains a list of poems, titled highlighted_poems.

Start by splitting highlighted_poems at the commas and saving it to highlighted_poems_list.
'''
highlighted_poems = "Afterimages:Audre Lorde:1997,  The Shadow:William Carlos Williams:1915, Ecstasy:Gabriela Mistral:1925,   Georgia Dusk:Jean Toomer:1923,   Parting Before Daybreak:An Qi:2014, The Untold Want:Walt Whitman:1871, Mr. Grumpledump's Song:Shel Silverstein:2004, Angel Sound Mexico City:Carmen Boullosa:2013, In Love:Kamala Suraiyya:1965, Dream Variations:Langston Hughes:1994, Dreamwood:Adrienne Rich:1987"
print(highlighted_poems)

highlighted_poems_list = highlighted_poems.split(',')
print(highlighted_poems_list)

'''
Notice that there is inconsistent whitespace in highlighted_poems_list. Let’s clean that up.

Start by creating a new empty list, highlighted_poems_stripped.
'''
highlighted_poems_stripped = []

for poem in highlighted_poems_list:
    highlighted_poems_stripped.append(poem.strip())

print(highlighted_poems_stripped)


'''
Iterate through highlighted_poems_stripped and split each string around the : characters and append the new lists into highlighted_poems_details.
'''

highlighted_poems_details = []

for poem in highlighted_poems_stripped:
    highlighted_poems_details.append(poem.split(':'))

print(highlighted_poems_details)

'''
Now we want to separate out all of the titles, the poets, and the publication dates into their own lists.
'''

titles = []
poets = []
dates = []

for details_list in highlighted_poems_details:
    titles.append(details_list[0])
    poets.append(details_list[1])
    dates.append(details_list[2])

'''
Finally, write a for loop that uses .format() to print out the following string for each poem:

The poem TITLE was published by POET in DATE.
'''

for i in range(len(titles)):
    print('The poem {title} was published by {poet} in {date}.'.format(
        title=titles[i], poet=poets[i], date=dates[i]))
